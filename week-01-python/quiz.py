questions = [
    {"question": "What is a token?", "answer": "a chunk of text"},
    {"question": "What is an API?", "answer": "a way for programs to talk to each other"},
    {"question": "What is a model?", "answer": "a system trained to make predictions"}
]

score = 0

for item in questions:
    user_answer = input(item["question"] + " ")
    if user_answer.lower().strip() in item["answer"].lower():
        score += 1

print(f"Score: {score}/{len(questions)}")