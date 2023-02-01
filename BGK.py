import random
from secrets import choice

print("Selamat Datang di Game AFRAAAA")



while True: 
    choices = ["batu","gunting","kertas"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("batu,gunting,kertas?:").lower()

    if player == computer:
        print("computer:",computer)
        print("player:",player)
        print("Seri!")

    elif player == "batu":
        if computer == "kertas":
            print("computer:",computer)
            print("player:",player)
            print("Player Lose !")
        if computer == "gunting":
            print("computer:",computer)
            print("player",player)
            print("Player Win ! ")

    elif player == "gunting":
        if computer == "batu":
            print("computer:",computer)
            print("player",player)
            print("Kalah CUPU !!!")
        if computer == "kertas":
            print("computer:",computer)
            print("player:",player)
            print("Anjaayyy Menang COkkk")

    elif player == "kertas":
        if computer == "gunting":
            print("computer:",computer)
            print("player",player)
            print("Kalah CUPU !!!")
        if computer == "batu":
            print("computer:",computer)
            print("player:",player)
            print("Anjaayyy Menang COkkk")


    play_again = input("Main lagi? (gas/gak):").lower()

    if play_again !="gas":
       break
print("oke byee")    
delay("3000")
# ****************************************************************

