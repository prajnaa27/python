import json

with open("quiz.json",'r') as file:
    content = file.read()

data = json.loads(content)

for quiz in data:
    print(quiz["quiz_text"])
    for i, choice in enumerate(quiz["choices"]):
        print(i+1, "-", choice)
    user_choice = int(input("Enter your answer:"))

