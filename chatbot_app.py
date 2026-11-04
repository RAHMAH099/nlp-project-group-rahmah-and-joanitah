import os
import numpy as np
import gradio as gr
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from huggingface_hub import InferenceClient

PDF_PATH = "document.pdf"
LLM_MODEL = "meta-llama/Llama-3.1-8B-Instruct"

SYSTEM_PROMPT = """
You are Health Guide Assistant, a polite and helpful document-based chatbot.

1. Answer questions about the uploaded document using ONLY the retrieved context.
2. Use conversation history to understand follow-up questions.
3. If a question is unrelated to the document, politely explain your purpose and redirect the user.
4. Respond politely to greetings.
5. Explain your identity when asked.
6. Remain professional when users are rude.
7. Never invent information.
8. Cite page numbers when providing document information.
9. If information is unavailable, clearly say so.
10. Returns the page number when answering questions using document information.

Your main purpose is to help users understand the uploaded health document.
"""

llm = InferenceClient(api_key=os.environ["HF_TOKEN"])   # read from the Space secret
embedder = SentenceTransformer("all-MiniLM-L6-v2")

pages = [(i + 1, p.extract_text() or "") for i, p in enumerate(PdfReader(PDF_PATH).pages)]
chunks = []
for page_num, text in pages:
    text = " ".join(text.split())
    for start in range(0, len(text), 400):
        piece = text[start:start + 500]
        if len(piece) > 50:
            chunks.append({"page": page_num, "text": piece})
vectors = embedder.encode([c["text"] for c in chunks], normalize_embeddings=True)

def retrieve(q, k=3):
    scores = vectors @ embedder.encode([q], normalize_embeddings=True)[0]
    return [chunks[i] for i in np.argsort(scores)[::-1][:k]]

def chat(message, history):
    context = "\n\n".join(f"[page {h['page']}] {h['text']}" for h in retrieve(message))
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history[-10:]
    messages.append({"role": "user", "content": f"Context:\n{context}\n\nQuestion: {message}"})
    r = llm.chat.completions.create(model=LLM_MODEL, messages=messages, max_tokens=400, temperature=0.2)
    return r.choices[0].message.content

gr.ChatInterface(fn=chat, type="messages", title="Health Guide Assistant").launch()
