import random
c_move,u_move =("","")
draw,win,lose,total_move = (0,0,0,0)
print(" WELCOME TO ROCK PAPER SCISSOR GAME ")

while True:
    u_move = input("Enter rock or paper or scissor,q for quit : ").lower().strip()
    if u_move not in {"rock","paper","scissor","q"}:
        continue
    elif u_move == "q":
        break
    else:
        c_move = random.choice(["rock","paper","scissor"])
        total_move =+1
        print(f" Your Move -> {u_move} \n Computer's Move -> {c_move} ")
        if c_move == u_move:
            print("     DRAW!...")
            draw +=1
        elif (u_move=="paper" and c_move=="rock") or (u_move=="scissor" and c_move=="paper") or (u_move=="rock" and c_move=="scissoer"):
            print("     VICTORY!... ")
            print("     HURRAY!! YOU WIN:-) ")
            win +=1
        else:
            print("     DEFEAT!... ")
            print("     BETTER LUCK NEXT TIME:-( ")
            lose +=1
print(f"You have {win} wins,{lose} loses,{draw} draws -> {total_move} total_moves \n")