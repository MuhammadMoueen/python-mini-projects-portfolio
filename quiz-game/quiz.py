# Simple Quiz Game (Console Based)

questions = {
    "What is the capital of France?": {
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    "Which language is used for web apps?": {
        "options": ["A. Python", "B. Java", "C. HTML", "D. All of these"],
        "answer": "D"
    },
    "What does CPU stand for?": {
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"],
        "answer": "B"
    }
}


def run_quiz():
    score = 0

    for question, data in questions.items():
        print("\n" + question)

        for option in data["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid! Enter A, B, C, or D only: ").upper()

        if user_answer == data["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer is:", data["answer"])

    print("\nQuiz Finished!")
    print("Your Score:", score, "/", len(questions))


run_quiz()
