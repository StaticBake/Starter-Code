#My first game
#Rock Paper Scissor game
#2022/01/07
#Nico


from random import choice                                                                           #Choice function from Random module imported
from time import sleep                                                                              #Sleep function from Time module imported


print ("\n \n \n")                                                                                  #Format
print ("#---------------------------------------------------------------------------------# \n")    #Pleasing format in the terminal

name = input("Please enter your name:   ")

print ("Welcome to my rock paper scissor game " + name +  "\n \n")                                 #Welcoming message

user_score = 0
computer_score = 0

while (True):

    computer_options = ["rock", "paper", "scissor", "flamethrower"]                                                         #list of options for the computer

    computers_choice = choice(computer_options)                                                                             #random.choice()

    users_choice = input("Type 'Rock', 'Paper', 'Scissor', 'q' to quit, 'r' to reset the score board or check the score board with 'score' :       ").lower()
    #Get the users input and tell them what they can type
    print("\n \n")                                                                                                          #Print 2 new lines
    

    if users_choice == "q":                                                                                                 #If the user wants to quit, it will break the loop.
        print("Thank you for playing, hope you enjoyed the game.\n")                                                        #Goodbye msg
        print(name + " Score ",user_score,end= "")  
        print("             VS           Computer Score  ",computer_score)
        print("*--------------------------------The End -----------------------------------*")                              #Asthetics
        break                                                                                                               #breaking the while loop

    elif users_choice == "score":
        print(name + " ",user_score)
        print("Computer ",computer_score)
        print("\n")
        continue

    elif users_choice == "r":
        user_score = 0
        computer_score = 0
        continue
    
    if users_choice == "rock" or users_choice == "paper" or users_choice == "scissor":
        print("\n")
        print(name + "s Choice:      ",users_choice)
        print("Computers Choice:    ",computers_choice)
        print("\n")

        if users_choice == computers_choice:
            print ("You and the computer are tied, 1 point for everone check under your seats!")
            user_score += 1
            computer_score += 1

        elif computers_choice == "rock" and users_choice == "paper" or computers_choice == "scissor" and users_choice == "rock" or computers_choice == "paper" and users_choice == "scissor":
            print ("You won!, 1 point to the human")
            user_score += 1

        elif computers_choice == "flamethrower" or computers_choice == "rock" and users_choice == "scissor" or computers_choice == "paper" and users_choice == "rock" or computers_choice == "scissor" and users_choice == "paper":
            print ("The mighty machine wins!, 1 point to the machine")
            computer_score += 1
    
        
    else:
         print ("Invalid input! Are you trying to cheat with random giberish ???")

    print("\n \n")

