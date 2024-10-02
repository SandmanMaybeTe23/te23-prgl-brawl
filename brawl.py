

from random import randint
import math
import time
player1_lives=1
player2_lives=1
healing2=False
healing1=False
doge1=False
doge2=False
healed1=0
healed2=0
player_name1=input("hello player one what is your name")
player_or_computer=input(f"{player_name1} do you wan another player to fight Y/N")
player2=False
player_class2=False
game_round=0
game="off"
player_or_computer_converter = str.upper(player_or_computer)
if player_or_computer == "Y":
    print("Good")
    player_name2=input("So what is player two name?")
    player2=True
elif player_or_computer== "N":
    print("you are now playing with computer")
    player_name2="SkyNet"
    player2=False
elif player_or_computer != "Y" or "N":
    print("i can under stand so your playing with computer")
    player_name2= "SkyNet"
    player2=False



player_class1=input(f"{player_name1} what class do you can pick from /S/ for solder and solder give you extra lives /M/ for medic  you  have less live but a chance to get live per round or /B/ for baller that you get less live but you can doge attacks").upper() 
print(f"{player_class1}")

if player_class1 == "S":
    player1_lives=30
    print(f"{player_name1} you have pick solder you have 20 lives")
elif player_class1 == "M":
    player1_lives=10
    healing1=True
    print(f"{player_name1} you have pick MEDIC you have 10 live and you can heal your self ")
elif player_class1 == "B":
    player1_lives=15
    doge1=True
    print(f"{player_name1} you have pick baller and you have 15 lives")


if player2 == True :
    player_class2=input(f"{player_name2} what class do you want /S/ for Solder /M/ for Medic /B/ for Baller").upper()

if player_class2 == "S":
    player2_lives=30
    print(f"{player_name2} you have pick solder you have 20 lives")
    game="on"
elif player_class2 == "M":
    player2_lives=10
    healing2=True
    print(f"{player_name2} you have pick MEDIC you have 10 live and you can heal your self ")
    game="on"
elif player_class2 == "B":
    player2_lives=15
    doge2=True
    print(f"{player_name2} you have pick baller and you have 15 lives")
    game="no"

if player2 == False :
    ai_class=randint(1,3)
    if ai_class==1:
        player2_lives=20
        print(f"{player_name2} has picket solder")
        game="on"
    elif ai_class == 2:
        player_class2=10
        healing2=True
        print(f"{player_name2} has picket Medic")
        game="on"
    elif ai_class==3:
        player2_lives=15
        doge2=True
        print(f"{player_name2} hasa picket baller")
        game="on"
    
    
while game == "on":
    game_round=+1
    player1_lost=False
    player2_lost=False
    print("Round staring in 3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(f"{player_name1} rolls")
    player1_roll=randint(1,6)
    print("4")
    time.sleep(0.5)
    print("6")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("5")
    time.sleep(0.5)
    print(f"{player1_roll}")
    time.sleep(1)
    print(f"{player_name2} is now rolling")
    player2_roll=randint(1,6)
    print("3")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("4")
    time.sleep(0.5)
    print("5")
    time.sleep(0.5)
    print("6")
    time.sleep(0.5)
    print(f"{player2_roll}")

    if player1_roll>player2_roll:
        player2_lives=-1
        player2_lost=True
        print(f"{player_name1} has won {game_round}")
    elif player1_roll<player2_roll:
        player1_lives =-1
        player1_lost=True
        print(f"{player_name2} has won {game_round}")
    elif player1_roll==player2_roll:
        print("NO one won :l")

    
    
    if healing1==True:
        healed1=randint(1,3)
   
    if  healed1 ==1:
        print(f"{player_name1} has healed 0 lives")
    elif healed1 ==2:
        player1_lives=+1
        print(f"{player_name1} has healed 1 lives")
    elif healed1 ==3:
        player1_lives =+2
        print(f"{player_name1} has healed 2 lives")
   
   
    if healing2==True:
        healed2=randint(1,3)
    
    if healed2 ==1:
        print(f"{player_name2} has healed 0") 
    elif healed2 ==2:
        player1_lives=+1
        print(f"{player_name2} has healed 1")
    elif healed2 ==3:
        player2_lives =+2
        print(f"{player_name2} has healed 2")
    
    if player1_lost==True: 
        doge1chance=randint(1,5)

    if doge1==True:
        doge1_success=doge1chance
    
    if doge1_success== 4 or 5 :
        player1_lives=+1
        print(f"{player_name1} doge the attack")
    elif doge1_success == 1 or 2 or 3 :
        print(f"{player_name1} did not doge")

        
    if player2_lost==True: 
        doge2chance=randint(1,5)

    if doge1==True:
        doge2_success=doge2chance
    
    if doge2_success== 4 or 5 :
        player2_lives=+1
        print(f"{player_name2} doge the attack")
    elif doge2_success == 1 or 2 or 3 :
        print(f"{player_name2} did not doge")
        

    

    if player1_lives ==0:
        print(f"{player_name2} won the game")
        game = "off"
    elif player2_lives==0:
        print(f"{player_name1} won the game")
        game = "off" 