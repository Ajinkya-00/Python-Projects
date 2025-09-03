def rps():
    while True:
        p1 = input("\nPlayer 1 (rock/paper/scissors or exit): ")

        if p1 == "exit":
            break
        
        p2 = input("Player 2 (rock/paper/scissors): ")

        if p1 == p2:
            print("Draw!")
        elif (p1 == "rock" and p2 == "scissors") or \
             (p1 == "paper" and p2 == "rock") or \
             (p1 == "scissors" and p2 == "paper"):
            print("Player 1 Wins 🎉")
        else:
            print("Player 2 Wins 🎉")

rps()
