
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
doge1chance=0
doge2chance=0
player1_lost = False 
player2_lost = False
player1_won = False
player2_won = False
win_st1 = 0
win_st2 = 0
NO_one_Won= False
winner2=0
winner1=0
player_name1=input("hello player one what is your name  ")
player_or_computer=input(f"{player_name1} do you wan another player to fight Y/N  ").upper()
player2=False
player_class2=False
game_round=0
game=0
if player_or_computer == "Y":
    print("Good")
    player_name2=input("So what is player two name? ")
    player2=True
elif player_or_computer== "N":
    print("you are now playing with computer")
    player_name2="SkyNet"
    player2=False
elif player_or_computer != "Y" or "N":
    print("i can under stand so your playing with computer")
    player_name2= "SkyNet"
    player2=False



player_class1=input(f"{player_name1} what class do you can pick from /S/ for solder and solder give you extra lives /M/ for medic  you  have less live but a chance to get live per round or /B/ for baller that you get less live but you can doge attacks but if you wanna pick The Must class that gives you extremely little lives but you get live and damage if you win you gain lives and damage /W/  ").upper() 

if player_class1 == "S":
    player1_lives=15
    print(f"{player_name1} you have pick solder you have 20 lives")
elif player_class1 == "M":
    player1_lives=5
    healing1=True
    print(f"{player_name1} you have pick MEDIC you have 10 live and you can heal your self ")
elif player_class1 == "B":
    player1_lives=10
    doge1=True
    print(f"{player_name1} you have pick baller and you have 15 lives")
elif player_class1 == "W":
    player1_lives= 3
    winner1=True
    print(f"{player_name1} you have pick THE must and you have 3 lives")




if player2 == True :
    player_class2=input(f"{player_name2} what class do you want /S/ for Solder /M/ for Medic /B/ for Baller or you can pick the Must class/W/ ").upper()

if player_class2 == "S":
    player2_lives=15
    print(f"{player_name2} you have pick solder you have 20 lives")
    game="on"
elif player_class2 == "M":
    player2_lives=5
    healing2=True
    print(f"{player_name2} you have pick MEDIC you have 10 live and you can heal your self ")
    game="on"
elif player_class2 == "B":
    player2_lives=10
    doge2=True
    print(f"{player_name2} you have pick baller and you have 15 lives")
    game="on"
elif player_class2 =="W":
     player2_lives=3
     winner2=True
     print(f"{player_name2} has picket Must")
     game="on"

    


if player2==False:
    ai_class=randint(1,4)
    
    if ai_class==1:
        player2_lives=15
        print(f"{player_name2} has picket solder")
        game="on"
    elif ai_class == 2:
        player_class2=5
        healing2=True
        print(f"{player_name2} has picket Medic")
        game="on"
    elif ai_class==3:
        player2_lives=10
        doge2=True
        print(f"{player_name2} has picket baller")
        game="on"
    elif ai_class == 4:
        player2_lives=3
        winner2=True
        print(f"{player_name2} has picket Must")
        game="on"
        
    

while game == "on":
    game_round+=1
    player1_lost=False
    player2_lost=False
    NO_one_Won= False
    player2_won = False
    player1_won = False
    print(f"{player_name1} has {player1_lives}")
    print(f"{player_name2} has {player2_lives}")
    print(f"the Round{game_round}")
    print("Round staring in 3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(f"{player_name1} rolls")
    player1_roll=randint(1,6)
    print("4")
    time.sleep(0.2)
    print("6")
    time.sleep(0.2)
    print("3")
    time.sleep(0.2)
    print(f"{player1_roll}")
    time.sleep(1)
    print(f"{player_name2} is now rolling")
    player2_roll=randint(1,6)
    print("3")
    time.sleep(0.2)
    print("5")
    time.sleep(0.2)
    print("6")
    time.sleep(0.2)
    print(f"{player2_roll}")
    
    
    if player1_roll>player2_roll:
        print(f"{player_name1} has won")
        player1_won=True
        win_st1+=1
        player2_lost=True
        if winner1 == True:
            player2_lives -= 1*win_st1
        else:
            player2_lives-= 1


    elif player2_roll>player1_roll:
        
        print(f"{player_name2} has won")
        player1_lost=True
        win_st2 +=1
        player2_won=True
        if winner2 == True:
            player1_lives-=1*win_st2
        else:
         player1_lives-=1
            
    elif player1_roll==player2_roll:
        print("NO ONE WON :L")
        NO_one_Won=True

    
    if healing2 == True and player2_lost == True:
        healed2=randint(1,3)
        if healed2==3 :
            player2_lives+=2
            print(f"{player_name2} has healed")

     
    if healing1 == True and player1_lost == True:
        healed1=randint(1,3)
        if healed1==3 :
            player1_lives+=2
            print(f"{player_name1} has healed")
    

    if doge2 == True and player2_lost == True:
        doge2chance=randint(1,5)
        if doge2chance== 5:
            player2_lives +=1
            print(f"{player_name2} has doge")
   
    if doge1 == True and player1_lost == True:
        doge1chance=randint(1,5)
        if doge1chance== 5 :
            player1_lives +=1
            print(f"{player_name1} has doge")

    if player1_won== True and winner1 == True:
        player1_lives += 1*win_st1
        win_st2=0
    elif player2_won== True and winner2 == True:
        player2_lives +=1*win_st2
        win_st1=0
    elif NO_one_Won== True:
        win_st1=0
        win_st2=0 
        



    if player1_lives ==0:
        print(f"{player_name2} won the game")
        game = "off"
    elif player2_lives==0:
        print(f"{player_name1} won the game")
        game = "off" 
    elif game_round == 40:
        game = "off"
        print("GGs no one won")
    



    