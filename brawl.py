

from random import randint
import math


player_name1=input("hello player one what is your name")
player_or_computer=input(f"{player_name1} do you wan another player to fight Y/N")


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
    player1_lives=20
    print(f"{player_name1} you have pick solder you have 20 lives")
elif player_class1 == "M":
    player1_lives=10
    healing=True
    print(f"{player_name1} you have pick MEDIC you have 10 live and you can heal your self ")
elif player_class1 == "B":
    player1_lives=15
    doge=True
    print(f"{player_name1} you have pick baller and you have 15 lives")


if player2 == True :
    player_class2=input(f"{player_name2} what class do you want /S/ for Solder /M/ for Medic /B/ for Baller").upper()

if player_class2 == "S":
    player1_lives=20
    print(f"{player_name2} you have pick solder you have 20 lives")
elif player_class2 == "M":
    player1_lives=10
    healing=True
    print(f"{player_name2} you have pick MEDIC you have 10 live and you can heal your self ")
elif player_class2 == "B":
    player1_lives=15
    doge=True
    print(f"{player_name2} you have pick baller and you have 15 lives")

if player2 ==False :
    aiclass=randint(1,3)
    if aiclass==1 :
        