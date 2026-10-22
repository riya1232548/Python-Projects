
def run_quiz():
    questions = [
        {
            "question": "Which programming language is commonly used for data analysis?",
            "options": [
                "A) HTML",
                "B) Python",
                "C) CSS",
                "D) XML"
            ],
            "answer": "B"
        },
        {
            "question": "Which SQL command is used to retrieve data from a table?",
            "options": [
                "A) UPDATE",
                "B) DELETE",
                "C) SELECT",
                "D) INSERT"
            ],
            "answer": "C"
        },
        {
            "question": "Which Python library is commonly used for data analysis?",
            "options": [
                "A) Pandas",
                "B) Turtle",
                "C) Pygame",
                "D) Tkinter"
            ],
            "answer": "A"
        },
        {
            "question": "What does a primary key do in a database?",
            "options": [
                "A) Deletes all records",
                "B) Identifies each record uniquely",
                "C) Sorts data automatically",
                "D) Creates charts"
            ],
            "answer": "B"
        },
        {
            "question": "Which tool is commonly used to create interactive data dashboards?",
            "options": [
                "A) Notepad",
                "B) Paint",
                "C) Power BI",
                "D) Calculator"
            ],
            "answer": "C"
        },
        {
            "question": "Which Python data structure stores key-value pairs?",
            "options": [
                "A) List",
                "B) Tuple",
                "C) Set",
                "D) Dictionary"
            ],
            "answer": "D"
        },
        {
            "question": "What does SQL stand for?",
            "options": [
                "A) Structured Query Language",
                "B) Simple Question Language",
                "C) Standard Python Library",
                "D) System Quality Logic"
            ],
            "answer": "A"
        },
        {
            "question": "Which chart is commonly used to show trends over time?",
            "options": [
                "A) Pie chart",
                "B) Line chart",
                "C) Table only",
                "D) Scatter chart only"
            ],
            "answer": "B"
        }
    ]

    score = 0

    print("================================")
    print("       PYTHON IT QUIZ")
    print("================================\n")

    for index, q in enumerate(questions):
        print(f"Q{index + 1}: {q['question']}")

        for option in q["options"]:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ")
        user_answer = user_answer.strip().upper()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! Correct answer: {q['answer']}\n")

    print("================================")
    print(f"Your final score is {score}/{len(questions)}")
    print("================================")


run_quiz()
