# Quize game 
print("Welcome to my game!")
play = input("DO you want to play: ")

if play.lower() != "yes":
    quit()

scours = 0

# Quiz start 1 
question1 = input("What is CPU stands for? ")
if question1.lower() == "central processing unit":
    print("Correct! ")
    scours += 1
else:
    print("Incorrect! ")
# 2
question2 = input("What is GPU stands for?: ")
if question2.lower() =="graphics processing unit":
    print("Correct!")
    scours += 1
else:
    print("Incorrect!")
# 3
question3 = input("What is HTML stands for?: ")
if question3.lower() =="hyper text markup language":
    print("Correct!")
    scours += 1
else:
    print("Incorrect!")

# 4
question4 = input("What is RAM stands for?: ")
if question4.lower() =="random-access memory":
    print("Correct!")
    scours += 1
else:
    print("Incorrect!")
# 5
question5 = input("What is USA stands for?: ")
if question5.lower() =="united states of america.":
    print("Correct!")
    scours += 1
else:
    print("Incorrect!")

print(f"Your scour is {scours}. :)")
print(f"You got {(scours / 5) * 100 }")
