def play_quiz(questions):
    score = 0

    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i+1}. {choice}")

        answer = int(input("Enter your answer (1-4): "))

        if answer == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        print()

    print("Quiz completed!")
    print(f"You scored {score}/{len(questions)}")

# Define the quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Rome", "London", "Berlin", "Paris"],
        "correct_answer": 4
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        "correct_answer": 1
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Mars", "Jupiter", "Saturn", "Earth"],
        "correct_answer": 2
    }
]

# Start the quiz
play_quiz(quiz_questions)
