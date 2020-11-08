#****************************************************
# program:          CamelGame.py
# prgrammer:        Evan Greager, Tyler Powell
# date:             
# updated:           
# Purpose:          A text game with a camel going across
#                   the Mobi desert.
# Required Modules: random
# Inputs:           letter choices
# Outputs:          Text messages
# Updates:
#
#*****************************************************


#Evan Greager
#Tyler Powell

import random
def quit():
    print("The program will now exit.")
    return True

def oasisFind(thirst,camelTiredness,drinks):
    oasis = random.randrange(20)
    if oasis == 10 :
        thirst = 0
        camelTiredness = 0
        drinks += 3
        print("As you travel you happen upon an oasis!")
        print("You fill your canteen and your stomach with water, and")
        print("Your camel is rested!")
        print("The natives continue the chase.")
        return thirst,camelTiredness,drinks
        print()
    else:
        return thirst,camelTiredness,drinks
        
def medSpeed(miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled):
    miles = random.randrange(7, 15)
    milesTraveled += miles
    thirst += random.randrange(0,2)
    camelTiredness += 1
    distanceRaidersTraveled += random.randrange(10, 16)
    print("You move forward at a moderate pace traveling",miles,"miles; a total of", milesTraveled, "miles traversed.")
    print("Your thirst increases.")
    print("The raiders continue their pursuit.")
    print()
    return miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled

def fullSpeed(miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled):
    miles = random.randrange(15, 25)
    milesTraveled += miles
    thirst += 1
    camelTiredness += random.randrange(1, 4)
    distanceRaidersTraveled += random.randrange(10, 16)
    print("You push onward at full speed covering",miles,"miles; a total of", milesTraveled, "miles traversed.")
    print("Your thirst increases.")
    print("The raiders continue their pursuit.")
    print()
    return miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled

def restStop(camelTiredness,distanceRaidersTraveled):
    print("You stop for the night.")
    print("Your camel is no longer tired.")
    print("The raiders have continued their pursuit during your rest.")
    print()
    camelTiredness = 0
    distanceRaidersTraveled += random.randrange(10, 16)
    return camelTiredness,distanceRaidersTraveled

def gameProceedCheck(milesTraveled,thirst,camelTiredness,distanceRaidersTraveled):
    
    #Thirst loss check
    if thirst > 5 :
        print("You died of thirst!")
        print("Game Over.")
        print()
        return True
    # Distance traveled win check
    elif milesTraveled >= 500 :
        print(
                """
                Congratulations! You have crossed the entire desert and
                successfully escaped the raiders!
                """
                )
        print("You win!")
        print()
        return True
    # Camel's tiredness loss check
    elif camelTiredness > 10 :
        print("Your camel died of exhaustion!")
        print(
                """
                With no camel, the raiders catch up to you, killing you ")
                and taking the diamond for themselves!
                """
                )
        print("Game Over.")
        print()
        return True
    # Natives loss check
    elif milesTraveled - distanceRaidersTraveled <= 0 :
        print("The raiders have caught up with you!")
        print("The raiders kill you and the diamond is theirs!.")
        print("Game Over.")
        print()
        return True
    
    #Warnings
    
    elif camelTiredness > 8 :
        print("Your camel shows signs of severe exhaustion")
    #Thirst warning
    if thirst > 4 :
        print("You are very thirsty! You feel you may die of thirst!")
    #Natives warning
    elif milesTraveled - distanceRaidersTraveled < 15 :
        print("You see faint shapes on the horizon behind you.")
        print("The raiders are closing in!")
        print()
    #Camel tiredness warning
    elif camelTiredness > 6 :
        print("Your camel is getting tired.")
        print()
    else:
        return milesTraveled,thirst,camelTiredness,distanceRaidersTraveled
        
def status(miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled,drinks):
    gameProceedCheck(milesTraveled,thirst,camelTiredness,distanceRaidersTraveled)
    print("Miles traveled:",milesTraveled)
    print("Drinks in canteen:",drinks)
    print("The raiders are",milesTraveled-distanceRaidersTraveled,"miles behind you.")
    print()
    return miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled,drinks




    
def main():
    restart="Y"
    while restart.upper()=="Y":
        choice = ""
        done = False  # loop variable
    
        #variables for game
        miles=0
        milesTraveled = 0
        thirst = 0
        camelTiredness = 0
        distanceRaidersTraveled = -25
        drinks = 3
        
        print(
                """
                Hail adventurer! In this text adventure, you are a jewel thief
                absconding on camelback across the 500-mile Mobi desert, with the rare 
                and coveted Pink Panther diamond! However, deadly raiders have 
                discovered the contents of your prized package, and are hot on 
                your tail to claim the jewel for themselves! 
                """
                )
        status(miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled,drinks)
        
        while not done:
            print(
            """
            A - Drink from you canteen.
            B - Move ahead at moderate speed. 
            C - Move ahead at full speed. 
            D - Stop and rest for night.
            E - Status check.
            Q - Quit the Game
            """
            )
    
            choice = input(" What will you do?\n")
            if choice.upper() == "Q":
                done = quit()
        
    
            elif choice.upper() == "A":
                if drinks>=0:
                    drinks-=1
                    thirst = 0
                    print("Your thirst has been quenched; you feel refreshed.")
                else:
                    print("You are out of water!")
    
            elif choice.upper() == "B":
                miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled = medSpeed(miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled)
                thirst,camelTiredness,drinks = oasisFind(thirst,camelTiredness,drinks)
                if gameProceedCheck(milesTraveled,thirst,camelTiredness,distanceRaidersTraveled)==True:
                    done=quit()
    
            elif choice.upper() == "C":
                miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled = fullSpeed(miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled)
                thirst,camelTiredness,drinks = oasisFind(thirst,camelTiredness,drinks)
                if gameProceedCheck(milesTraveled,thirst,camelTiredness,distanceRaidersTraveled)==True:
                    done=quit()
                
            elif choice.upper() == "D":
                camelTiredness,distanceRaidersTraveled=restStop(camelTiredness,distanceRaidersTraveled)
                if gameProceedCheck(milesTraveled,thirst,camelTiredness,distanceRaidersTraveled)==True:
                    done=quit()
                
            elif choice.upper() == "E":
                status(miles,milesTraveled,thirst,camelTiredness,distanceRaidersTraveled,drinks)
                
            else:
                print("That was not a correct choice - Enter (A through E or Q)")
        restart=input("Restart game? [Enter 'Y' to restart, or enter any key to exit.]\n")  
        
# call main
main()
    