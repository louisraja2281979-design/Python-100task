# Quiz Application

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. HTML", "B. Java", "C. Python", "D. CSS"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": [
            "A. Dennis Ritchie",
            "B. James Gosling",
            "C. Guido van Rossum",
            "D. Bjarne Stroustrup"
        ],
        "answer": "C"
    }
]

score = 0

print("=== Welcome to the Quiz Application ===\n")

for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}\n")

print("=== Quiz Completed ===")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("🏆 Excellent!")
elif percentage >= 50:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")