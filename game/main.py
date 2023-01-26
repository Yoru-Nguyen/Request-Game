from art import logo
from art import vs
from data import data
import random
import time
import os 
def fomat_data(account):
#Format the account data into printable format
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_des}, from {account_country}")

#
def check_answer(guess,account_a,account_b):
    check = False
    if account_a["follower_count"] > account_b["follower_count"] and guess == 'A':
        print("Good job !!!\n")
        check = True
    elif account_b["follower_count"] > account_a["follower_count"] and guess == 'B':
        print("Good job !!!\n")
        check = True
    else:
        print("Wrong !!!\n")
        check = False
    return check  
 
#Main
if __name__ == "__main__":
    score = 0
    #Play the game until press E or turn of the game
    while(True):
        # Generate a random account from the game data
        account_a = random.choice(data)
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)   
        #print the logo from file art.py
        print(logo)
        
        print(f"Account a: {fomat_data(account_a)}")
        print(vs)
        print(f"Account b: {fomat_data(account_b)}\n")
        print("--------------------Who have more followers ?--------------------")
        print("|                                                                |")
        print("|    Chose Account a press A                                     |")
        print("|                                                                |")
        print("|    Chose Account B press B                                     |")
        print("|                                                                |")
        print("|    Want to exit press E                                        |")
        print("|                                                                |")
        print("-----------------------------------------------------------------\n")
        guess = input("Type here: ")
        if guess == 'E':
            break
        if check_answer(guess,account_a,account_b) == True:
            score += 1
        print("----------------------------------")
        print(f"|Your score is ==> {score}\t\t |")
        print("----------------------------------\n")
        time.sleep(3)
        os.system("cls") # Windows
        os.system("clear") # Mac OS / Linux 
    
    
    


