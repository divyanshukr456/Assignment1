def quiz_app():
    questions = {
        "What is 2+2?": "4",
        "What is the capital of France?": "Paris",
        "Is Python a programming language? (yes/no)": "yes"
    }
    score = 0
    for q, a in questions.items():
        ans = input(q + " ")
        if ans.lower().strip() == a.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was {a}.")
    print(f"Your final score is {score}/{len(questions)}")
if __name__ == '__main__':
    quiz_app()
