import random

while True:
    print("rock,paper, scessiot")

    user_score = 0
    comp_score = 0
    ties = 0

    print(""" 
    1.Paper vs Rock ---> Paper
    2. Rock vs Scissors --> Rock 
    3. Scisssors vs Paper ---> Scissors""")

    name = input("Enter your name here: ")
    print(""" Choices are:
    1.Rock
    2.Paper
    3.Scissors""")
    choice = int(input("Enter your choice form 1-3: "))
    print()
    while choice > 3 or choice < 1:
        choice = int(input("Enter Valid Input"))

    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    print("The User's choice is ", user_choice)
    print("Now it is Computer's turn")


    computer = random.randint(1,3)

    if computer == 1: 
        comp_choice = "Rock"
    elif computer ==2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"

    print("The computer's choice is ",comp_choice)

    if ((user_choice == "Paper" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Paper")):
        print("Paper Wins")
        result = "Paper"
    elif ((user_choice == "Scissors" and comp_choice == "Rock") or (user_choice == "Rock" and comp_choice == "Scissors")):
        print("Rock Wins")
        result = "Rock"
        
    elif(user_choice == comp_choice):
        print("it's a tie")
        result = "Tie"
    

    else:
        print("Scissors Wins")
        result = "Scissors"


    if result == "Tie":
        ties += 1
    elif result == user_choice:
        user_score += 1
    else:
        comp_score += 1


    print("Scores are")
    print("user score is ", user_score)
    print("computer's score is ", comp_score)
    print("ties are ", ties)
    
    repeat = input("do you want to play agin? ")
    if repeat == "no" or repeat == "No":
        break


print ("game over ")
print("Thanks for playing")