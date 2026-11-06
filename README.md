# Group NLP Project

**Course:** Applied Data Science WITI C5 — NLP End-of-Module Project  
**Deadline:** 7th November 2026, 23:59  
**Members:** Joanitah Nattabi  and Rahmah Namugwanya

---

## App 1: Sentiment Analyser

The Sentiment Analyser is an NLP application that classifies movie reviews according to their sentiment.

- **Model:** [Rahmah and Joanitah's Sentiment Analysis Model](https://huggingface.co/RahmahwithCode/rahmahandjoanitah-sentiment-model)
- **Screenshots:** `screenshot1.jpeg`, `screenshot2.jpeg`
- **Test Accuracy:** 0.9140 (91.40%)
- **Test F1 Score:** 0.9140 (91.40%)

### How to Run the API

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn main:app --reload
```

API interactive documentation is available at:

`http://127.0.0.1:8000/docs`

### Example Prediction

- **Request:** Send `POST {"text": "I love this"}` to `/predict`.
- **Response:** `{"label": "POSITIVE", "score": 0.9921}`

### Example Predictions

| Review | Predicted Sentiment | Score |
|---|---|---|
| This movie was fantastic! The acting was brilliant. | POSITIVE | 0.9983 |
| Terrible experience, I want my money back. | NEGATIVE | 0.9973 |
| The movie was okay, but the story was predictable. | NEGATIVE | 0.9988 |

---

## App 2: Document Chatbot

The Document Chatbot uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from a supplied document and answer users' questions based on its contents.

- **Document Used:** Healthy Living Guide 2020–2021
- **Screenshots:** `screenshot3.jpeg`, `screenshot4.jpeg`

### Test Results

The following five questions were used to evaluate the chatbot's ability to retrieve information and provide relevant answers from the document.
| Question | Right page found? | Retrieved Page(s) | Answer correct? | Invented anything? |
| :--- | :--- | :--- | :--- | :--- |
| **1. What types of exercises can I do?** | Yes | Page 18, 23 | Yes | No |
| **2. What can one do to maintain good health?** | Yes | Page 1 | Yes | No |
| **3. What foods can one eat to also maintain good health?** | Yes | Page 1, 2 | Yes | No |
| **4. What time do lessons start at my school?** | N/A (not in PDF) | None | Correct (says "I don't know") | No |
| **5. Have I taken lunch today?** | N/A (not in PDF) | None | Correct (says "I don't know") | No |

### What Broke and How We Fixed It

---

## Our Model vs the LLM

- **Latency & Speed:** Our fine-tuned DistilBERT processes inference in approximately 15–30 ms per review on GPU and 80 ms on CPU, making it roughly 10 to 20 times faster than cloud LLM API calls over HTTPS.
- **Cost:** Once fine-tuned, DistilBERT can run locally or on low-cost computing resources without recurring per-token API costs.
- **Privacy & Security:** DistilBERT can run locally without exposing sensitive user reviews or customer feedback to external third-party endpoints.
- **Offline Reliability:** DistilBERT can operate in offline environments, whereas cloud-based LLM APIs require internet connectivity.
- **Generality vs Specialisation:** LLMs provide open-ended reasoning, while our specialised DistilBERT model is optimised for sentiment classification, achieving 91.40% test accuracy.

---

## Limitations

- **Domain & Language Constraint:** The model was trained predominantly on English movie reviews (`stanfordnlp/imdb`). Its performance may decrease on non-English text, Luganda expressions, and local informal colloquialisms.
- **Sarcasm & Subtlety:** Highly sarcastic reviews, such as *"What a breathtaking waste of two hours of my life"*, can sometimes be difficult to classify correctly.
- **RAG Document Boundary:** The document chatbot is limited to the information contained in the supplied Healthy Living Guide. It may not answer questions outside the document.

---

## Who Did What

### Member A: Joanitah Nattabi (`nattabijoanitah`)

- Fine-tuned the DistilBERT sequence classification model on the IMDb dataset using Google Colab.
- Computed and validated the test metrics (Accuracy: 0.9140, F1 Score: 0.9140).
- Contributed to publishing the sentiment model on the Hugging Face Hub.
- Developed the FastAPI microservice (`main.py`) with input validation and `/health` endpoints.

### Member B: Rahmah Namugwanya

- Built the document ingestion and retrieval pipeline using `pypdf` and `sentence-transformers` over the supplied document.
- Implemented the interactive Gradio interfaces (`app.py` for Sentiment Analysis and `chatbot_app.py` for Document RAG).
- Conducted the chatbot tests and evaluated the five-question benchmark.
- Recorded and validated all four submission screenshots and structured the GitHub repository.

---

## Project Screenshots

### Sentiment Analyser

![Sentiment Analyser Screenshot 1](screenshot1.jpeg)

![Sentiment Analyser Screenshot 2](screenshot2.jpeg)

### Document Chatbot

### Document Chatbot

![Document Chatbot Screenshot 1](screenshot3.jpeg)

![Document Chatbot Screenshot 2](screenshot%204.jpeg)
