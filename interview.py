# AI Interview System

questions = [
    {
        "question": "What is Python?",
        "keyword": "programming"
    },
    {
        "question": "What is SQL used for?",
        "keyword": "database"
    },
    {
        "question": "What is Machine Learning?",
        "keyword": "data"
    }
]

score = 0

print("===== AI Interview System =====")
name = input("Enter Candidate Name: ")

for q in questions:
    print("\nQuestion:", q["question"])
    answer = input("Your Answer: ").lower()

    if q["keyword"] in answer:
        print("Good Answer ✓")
        score += 1
    else:
        print("Answer Recorded")

print("\n===== Interview Result =====")
print("Candidate:", name)
print("Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 70:
    print("Result: Selected")
elif percentage >= 40:
    print("Result: Considered")
else:
    print("Result: Not Selected")