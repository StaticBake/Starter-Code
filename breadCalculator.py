# Welcome msg
print("\n\n")
print ("Welcome to the bread calculator, I can calculate ingredient weights for you.")
print("\n\n")

# Variables and inputs from user main loop start
#Main while loop
while True:

    while True:
        #making all input text lowerase and detrmine if the user is using a pan or not. Used try except to make sure the program doesn't crash if the user types in text instead of integres.
        using_pan = input("Are you using a pan to bake in?  (Yes/No) (q to quit):        ").lower()

        if using_pan == "yes":
            pan_ml = input("What is the pans volume in \"ml\"? :      ")
            try:
                pan_ml = int(pan_ml)
            except ValueError:
            #continue will take the program back to the start of the loop is the user type in somthing unwanted
                print("Please enter a number, no spaces or anything else!")
                continue
            #Change the string input to int for calculations and go out of the loop with break
            pan_ml = int(pan_ml)
            break

        elif using_pan == "no":
            bread_g = input ("Please enter the weight you want your bread to be in grams:        ")
            try:
                bread_g = int(bread_g)
            except ValueError:
                print("Please enter a number, no spaces or anything else!")
                continue
            bread_g = int(bread_g)
            break

        elif using_pan == "q":
            print("\nBye\n")
        #quit() exits the program
            quit()
        else: 
            print("Invalid input, Enter \'Yes\' or \'No\' no space or anything else")
            continue
# This loop gets the persentages of the ingredients from the user to calculate weights later
    while True:
    
        water = input("Please enter the %  water you want to use :                                                                         ")
        try :
            water = int(water)
        except ValueError:
            print("Only type a number!")
            continue

        salt = input("Please enter the %  salt you want to use(usually 2%):                                                               ")
    
        try :
            salt = int(salt)
        except ValueError:
            print("Only type a number!")
            continue

        yeast = input("Please enter the % yeast/sourdoug starter you want to use (usually 1-2% for dry yeast and 15-20% for the SS):       ")

        try :
            yeast = int(yeast)
        except ValueError:
            print("Only type a number!")
            continue

        water = int(water)
        salt = int(salt)
        yeast = int(yeast)

        if type(water) == int and type(salt) == int and type(yeast) == int:
            persentages = [water,salt,yeast]
            break

        else:
            print ("Please enter numbers, no spaces or text!")
            continue


# Calculations

    if using_pan == 'yes':
        pan_bread_g = (pan_ml/4)
        flour_g = (pan_bread_g/(100+persentages[0]+persentages[1]+persentages[2])*100)

    else:
    
        flour_g = (bread_g/(100+persentages[0]+persentages[1]+persentages[2])*100)

    water_g = (persentages[0]/100)*flour_g
    salt_g    = (persentages[1]/100)*flour_g
    yeast_g   = (persentages[2]/100)*flour_g

#Feedback

    print ('\n\n')
    print("You will need:         \n" + "Flour  " + str(round(flour_g,2))+"g" + "\n" + "Water   " + str(round(water_g,2))+'g' + "\n" + "Salt     " + str(round(salt_g,2))+'g' + "\n" + "Yeast    " + str(round(yeast_g,2))+'g')
    print ('\n\n')
