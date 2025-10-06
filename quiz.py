questions = (("Which animal is the largest on earth?"), 
             ("How many elements are in the periodic table?"),
             ("Which planet in our solar system is the largest?"),
             ("What is the most abundant gas in our atmosphere?"),
             ("What is the capital of Uzbekistan?")) 
options = (("A. Elephant ", "B. Blue whale ", "C. Lion ", "D. Shark "),
           ("A. 116 ", "B. 117 ", "C. 118 ", "D. 119 "),
           ("A. Jupiter ", "B. Saturn ", "C. Neptune ", "D. Uranus "),
           ("A. Carbon-dioxide ", "B. Nitrogen ", "C. Oxygen ", "D. Hydrogen "),
           ("A. Nukus ", "B. Samarkand ", "C. Bukhara ", "D. Tashkent "))  
answers = ("B", "C", "A", "B", "D") 
guesses = []
score = 0 
question_num = 0


for question in questions:
    print("---------------------------")
    print(question) 
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D):  ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1 
        print("CORRECT!")
    else:
        print("Unfortunately, that's INCORRECT.")
        print(f"{answers[question_num]} is the CORRECT answer.")
    question_num += 1 

print("---------------------------") 
print("------------ RESULTS -----------") 
print("---------------------------") 
print("Answers: ", end="")  
for answer in answers: 
    print(answer, end=" ") 
print()

print("Guesses: ", end="")  
for guess in guesses: 
    print(guess, end=" ") 
print() 

score = int(score / len(questions) * 100) 
print(f"Your score is {score}%")
