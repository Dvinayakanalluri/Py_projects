
Questions = (
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?"
)
Options = (
    ("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
    ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
    ("A. Ag", "B. Au", "C. Al", "D. Fe")
)

Answers = ( 
    "C",
    "B",
    "B"
)
guess = []
score = 0
question_num = 0

for question in Questions:
    print("\n" + question)
    for option in Options[question_num]:
        print(option)
    
    user_guess = input("Enter your answer (A, B, C, or D): ").upper()
    guess.append(user_guess)
    
    if user_guess == Answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {Answers[question_num]}.")
    
    question_num += 1

print("\n--- Quiz Results ---")
for i in range(len(Questions)):
    print(f"Question {i + 1}: {Questions[i]}")
    print(f"Your answer: {guess[i]}")
    print(f"Correct answer: {Answers[i]}\n")    
print(f"Your final score is: {score}/{len(Questions)}")   

