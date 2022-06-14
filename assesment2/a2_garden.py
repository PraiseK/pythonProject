"""
CP1401 2022-1 Assignment 2
Market Garden Simulator
Student Name: Praise Rudairo Kamusasa
Date started: 25/04/2022

Pseudocode:

 print(welcome, plant name, rainfall, food and cost, etc)
 import random from python libraries we can use later
 menu   =   create   menu   of   options   ("(W)ait",   "(D)isplay   plants",   "(A)dd   newplant", "(Q)uit")
 menu_check = input choices from ('w', 'd', 'a', 'q')
 plantlist = list the plant ["Parsley", "Sage", "Rosemary", "Thyme"]
 day = 0 (to start from zero)
 food = 0(to start from zero)
 
 function main_1  rainfall():
 rainfall = get_random_number(0, 100)
 print(actual_rainfall)
 if actual_rainfall < low rainfall threshold(30mm):
 plant_death = get_random_plant (0, length of plantlist with len() ) (tocatch random plant to die)
 if length of plantlist (with len())> 1:
 print(what plant has died, meanwhile the plant is deleted with pop())
 elif length of plantlist (with len()) == 1:
 print(the same as above, and plantlist becomes empty)
 else:
 print(Plantlist empty, No food produces and no plant dies)
 elif actual_rainfall >= low rainfall threshold(30mm):
 if length of plantlist (with len()) == 0:
 print(plantlist empty None produced)
 return actual_rainfall(to reread the actual_rainfall and calculate the newvalue)

    def simulate():
      if len(plantlist) != 0:        
      print("You finished with these plants: \n"+", ".join(plantlist))        
      result_print ()        
      print("Thank you for simulating. Now go and enjoy a real garden.")            
      else:        
      print("You finished with no plant")        
      result_print ()        
      print("Thank you for simulating. Now go and enjoy a real garden.")

      choice = input("Choose: ").lower()    
      if choice in menu_check:                
      plantlist.sort(key = lambda i: len(i))        
      if choice == 'w':                        
      day += 1             
      gen_food(actual_rainfall())                    
      elif choice == 'd':            # print two conditions if length of plantlist is equal to zero or not            
      if len(plantlist)!=0:                
      print(", ".join(plantlist))            
      else:                
      print("Plantlist is empty")                        
      elif choice == 'a':            
      add_new_plant()                                                

"""

import random

INFORMATION = "Welcome to my garden.\nPlants cost and generate food according to their name length (e.g., Sage plants cost 4).\n" \
              "You can buy new plants with the food your garden generates.\nYou get up to 128 mm of rain per day. " \
              "Not all plants can survive with less than 32.\nnEnjoy :)"
MENU = "(W)ait\n(D)isplay plants\n(A)dd   new plant\n(Q)uit"

MAX_RAIN = 128
MIN_RAIN = 32

# plant_food = []

print(INFORMATION)
choice = input("Would you like to load your plants from plants.txt (Y/n)?: ")
if choice == "n":
    in_file = open("plants")
    text = in_file.read()
    print(text)

else:
    print("Loaded")

day = 0
food = 0


def menu():
    plant_number = len(in_file.readlines())
    print(f"After {day} days, you have plants {plant_number} plants and your total food is {food} ")
    print(MENU)


def rainfall():
    random_rainfall = random.randint(0, MAX_RAIN)
    print(f"Rainfall: {random_rainfall}mm")
    if random_rainfall < MIN_RAIN:
        plant_death = random_plant_chosen()
        if len(in_file) > 1:
            print(f"Sadly, your {plant_death} plant has died")
            in_file.truncate(plant_death)
        elif len(in_file) == 1:
            print(f"Sadly, your {plant_death} plant has died.")
            in_file.truncate(plant_death)
        else:
            print("Plantlist is empty")


def random_plant_chosen():
    random_plant = random.randint(0, len(in_file))
    return random_plant


def plant_food():
    for plant in in_file:
        percent = random.randint(1 / 3 * rainfall(), rainfall() / 128)
        food_produced = percent * len(plant)
        return food_produced


def simulate():
    if len(in_file) != 0:
        print("You finished with these plants: \n" + ", ".join(in_file))
        print("Thank you for simulating. Now go and enjoy a real garden.")
    else:
        print("You finished with no plant")
        print("Thank you for simulating. Now go and enjoy a real garden.")


def main():
    print(menu())
    menu_choice = input("Choose: ").lower()
    if menu_choice == "d":
        print(text)
        print(menu())
        menu_choice = input("Choose: ").lower()
    elif menu_choice == "a":
        plant = input("Plant: ").isalpha()
        if plant not in in_file:
            cost = len(plant)
            if cost <= food:
                food -= cost
                in_file.write(plant)
            else:
                print(f"{plant} will cost {cost} food. With only {food}, you can't afford it.")
        elif plant in in_file:
            print(f"You already have a {plant} plant.")
        else:
            print("Invalid plant name name")
            menu_choice = input("Choose: ").lower()
    elif menu_choice == "w":
        day += 1
        print(rainfall())
    elif menu_choice == "q":
        print(simulate())


main()
