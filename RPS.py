import random
import time
from colorama import Fore, Back, Style
import os

def t5():
    time.sleep(.5)
def t():
    time.sleep(5)
def cls():
    os.system('cls||clear')
def enter():
    print("")
def white():
    print(Fore.WHITE)
def tc():
    time.sleep(5)
    os.system('cls||clear')
def rpsgame():
    tc()
    rps = ["Rock", "Paper", "Scissors"]
    rrps = random.choice(rps)
    rpsa = input(Fore.GREEN + "System: Type 'Rock', 'Paper' or 'Scissors': ")
    white()
    tc()
    if rpsa == rrps:
        print("*Demon chooses " + rrps)
        tc()
        print("We tied? That's no fun, let's go again.")
        rpsgame()
    elif rpsa == "Rock" and rrps == "Paper":
        print("*Demon chooses " + rrps)
        tc()
        print("*Demon pull out a glock and says, 'Sorry kid, I only play high stakes.'")
        tc()
        print(Fore.RED + "*Demon shoots you with the glock, shattering your soul")
        tc()
        print(Fore.GREEN + "System: You have reached a bad ending please try again.")
        tc()
        exit()
    elif rpsa == "Rock" and rrps == "Scissors":
        print("*Demon chooses " + rrps)
        tc()
        print("Hmmm, you actually won... I guess I'll be nice and give you your body back.")
        tc()
        print(Fore.BLUE + "*Demon ressurects your body and places your soul back where it belongs.")
    elif rpsa == "Scissors" and rrps == "Paper":
        print("*Demon chooses " + rrps)
        tc()
        print("Hmmm, you actually won... I guess I'll be nice and give you your body back.")
        tc()
        print(Fore.BLUE + "*Demon ressurects your body and places your soul back where it belongs.")
    elif rpsa == "Scissors" and rrps == "Rock":
        print("*Demon chooses " + rrps)
        tc()
        print("*Demon pull out a glock and says, 'Sorry kid, I only play high stakes.'")
        tc()
        print(Fore.RED + "*Demon shoots you with the glock, shattering your soul")
        tc()
        print(Fore.GREEN + "System: You have reached a bad ending please try again.")
        tc()
        exit()
    elif rpsa == "Paper" and rrps == "Rock":
        print("*Demon chooses " + rrps)
        tc()
        print("Hmmm, you actually won... I guess I'll be nice and give you your body back.")
        tc()
        print(Fore.BLUE + "*Demon ressurects your body and places your soul back where it belongs.")
    elif rpsa == "Paper" and rrps == "Scissors":
        print("*Demon chooses " + rrps)
        tc()
        print("*Demon pull out a glock and says, 'Sorry kid, I only play high stakes.'")
        tc()
        print(Fore.RED + "*Demon shoots you with the glock, shattering your soul")
        tc()
        print(Fore.GREEN + "System: You have reached a bad ending please try again.")
        tc()
        exit()
    else:
        rpsgame()
print("Lore: You have died; and are playing a game of rock paper scissors to see if you get to live")
tc()
print("Let's play a friendly game of rock, paper, scissors.")
rpsgame()
tc()