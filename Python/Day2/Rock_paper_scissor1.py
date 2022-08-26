def rock_paper_scissor(player1,player2):
    if(player1=="paper" and player2=="rock") or(player1=="scissor" and player2=="paper")or (player1=="rock" and player2=="scissor"):
        return "player1 wins"
    elif(player1=="rock" and player2=="paper") or(player1=="paper" and player2=="scissor") or (player1=="scissor" and player2=="rock"):
        return "player2 wins"
    else:
        return "nothing wins,match was tie"
