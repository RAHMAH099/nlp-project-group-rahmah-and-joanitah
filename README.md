# nlp-project-group-rahmah-and-joanitah
This is a repository containing the the sentiment analysis for nlp group work.


# Group NLP Project

Members: _Rahmah_Namugwanya___ and _Joanitah_Nattabi___

## App 1: Sentiment analyser
- Model: https://huggingface.co/RahmahwithCode/rahmahandjoanitah-sentiment-model
- Screenshots: screenshot1.png, screenshot2.png
- Test accuracy: __0.91%__ Test F1: _0.91%___
- How to run the API: pip install -r requirements.txt
uvicorn main:app --reload
- Example:
- | Review | Predicted sentiment | Score |
|---|---|---|
| This movie was fantastic! The acting was brilliant. | POSITIVE | 0.9983 |
| Terrible experience, I want my money back. | NEGATIVE | 0.9973 |
| The movie was okay, but the story was predictable. | NEGATIVE | 0.9988 |
  
## App 2: Document chatbot
- Screenshots: screenshot3.png, screenshot4.png
- Document used: _HeatlhyLivingGuide20-21__
- Test results:
- # QUESTIONING THE LLM QUESTIONS FROM THE PDF.
Q1: What types of exercises can I do?
A: Based on the information provided in the context, there are four main types of exercises:

1. **Lar Physical Activity**: This includes activities that are intense enough and last long enough to improve heart and lung fitness. Examples include walking, jogging, dancing, bicycling, basketball, soccer, and swimming.

2. **Muscle-Strengthening Activity**: Also known as resistance training, these activities help maintain or increase muscle strength, endurance, and power. Examples include using weight machines, free weights, resistance elastic bands, Pilates, and performing daily activities such as lifting children.

3. **Balance Training**: These activities aim to throw off one's balance to improve body control and stability. Examples include dynamic stretches performed with movement, static stretches held for several seconds or longer, passive stretching where an external force holds a pose, and active stretching without an external force.

4. **Flexibility Exercises**:
   - **Dynamic Stretches**: Performed with movement.
   - **Static Stretches**: Held for several seconds or longer.
   - **Passive Stretching**: Using an external force like a strap or wall to hold an elongated pose.
   - **Active Stretching**: Holding a pose without an external force.

The context also mentions combining exercise with a sedentary activity, suggesting ways to incorporate movement into everyday tasks, such as doing basic exercises like squats, marching in place, jumping jacks, push-ups, or sit-ups while watching TV or during commercials. Additionally, it provides resources for finding classes or events related to fitness, including checking schedules at gyms, yoga studios, or community centers. 

Q2: What can one do to maintain good health?
A: One can maintain good health by eating a healthy diet, exercising regularly, keeping a healthy body weight, not drinking too much alcohol, and not smoking. 

Q3: What foods can one eat to also maintain good health?
A: One can eat fruits and vegetables as they are rich in vitamins and minerals which contribute to maintaining good health. 

Q4: What time do lessons start at my school?
A: I don't know, that is not in the document. 

Q5: Have I taken lunch today?
A: I don't know, that is not in the document.
- What broke and how we fixed it:

  
## Our model vs the LLM
<your answer to the discussion question>
## Limitations

## Who did what
- Member A: __Rahmah_Namugwanya__
- Member B: _Joanitah_Nattabi__
