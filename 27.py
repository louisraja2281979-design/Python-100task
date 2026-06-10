import time

# Sample text
text = "Python is a powerful and easy to learn programming language."

print("=== Typing Speed Test ===")
print("\nType the following sentence:\n")
print(text)

input("\nPress Enter when you are ready...")

# Start timer
start_time = time.time()

# User input
typed_text = input("\nStart typing:\n")

# End timer
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

# Calculate WPM
word_count = len(typed_text.split())
wpm = (word_count / time_taken) * 60

# Calculate accuracy
correct_chars = 0
for i in range(min(len(text), len(typed_text))):
    if text[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(text)) * 100

# Display results
print("\n=== Results ===")
print(f"Time Taken: {time_taken:.2f} seconds")
print(f"Typing Speed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")