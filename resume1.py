# AI Resume Analyzer

keywords = [
    "python",
    "java",
    "sql",
    "machine learning",
    "communication",
    "teamwork"
]

print("===== AI Resume Analyzer =====")

resume_text = input("Paste Resume Text:\n").lower()

score = 0
found_keywords = []

for keyword in keywords:
    if keyword in resume_text:
        score += 1
        found_keywords.append(keyword)

print("\n===== Analysis Result =====")
print("Keywords Found:", ", ".join(found_keywords))
print("Score:", score, "/", len(keywords))

percentage = (score / len(keywords)) * 100
print("Match Percentage:", round(percentage, 2), "%")

if percentage >= 70:
    print("Result: Strong Resume")
elif percentage >= 40:
    print("Result: Average Resume")
else:
    print("Result: Needs Improvement")