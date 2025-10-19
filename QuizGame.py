print("Welcome to the QUIZ game!")
print("------------------------------")

score=0
playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time. Goodbye!")
    exit()

print("Great! Let's start the quiz.")

print("Question 1: What is the capital of France?")
answer1 = input("a) Berlin\nb) Madrid\nc) Paris\nd) Rome\nYour answer: ")
if answer1.lower()=="paris" or answer1.lower()=="c":
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is c) Paris.")

print("Question 2: What is 5 + 7?")
answer2 = input("a) 10\nb) 11\nc) 12\nd) 13\nYour answer: ")
if answer2.lower()=="12" or answer2.lower()=="c":
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is c) 12.")

print("Question 3: Who wrote 'Hamlet'?")
answer3 = input("a) Charles Dickens\nb) William Shakespeare\nc) Mark Twain\nd) Jane Austen\nYour answer: ")
if answer3.lower()=="william shakespeare" or answer3.lower()=="b":
    print("Correct!")
    score+=1    
else:
    print("Wrong! The correct answer is b) William Shakespeare.") 

print("How many continents are there on Earth? ")
answer4 =  input("a) 5\nb) 6\nc) 7\nd) 8\nYour answer: ")
if answer4.lower()=="7" or answer4.lower()=="c":
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is c) 7.")

print("Which planet is known as the “Red Planet”?")
answer5 = input("a) Earth\nb) Mars\nc) Jupiter\nd) Saturn\nYour answer: ")
if answer5.lower()=="mars" or answer5.lower()=="b":
    print("Correct!")
    score+=1
else:
    print("Wrong! The correct answer is b) Mars.")

print("------------------------------")

print(f"You got {score} out of 5 questions correct.")
percentage = (score / 5) * 100  
print(f"Your score: {percentage}%")