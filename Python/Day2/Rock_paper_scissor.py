n=0

while(n<100):

    choice = input("do you want to continue press yes or no:")

    if(choice=="yes"):
        player1 = input("enter your choice:")
        player2 = input("enter your choice:")
        if (player1 == "paper" and player2 == "rock") or (player1 == "scissor" and player2 == "paper") or (
                player1 == "rock" and player2 == "scissor"):
            print("player1 wins")
        elif (player1 == "rock" and player2 == "paper") or (player1 == "paper" and player2 == "scissor") or (
                player1 == "scissor" and player2 == "rock"):
            print("player2 wins")
        else:
           print("nothing win's the game,It's tie")
    print("thankyou for visiting!")