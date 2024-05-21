import AgnostGame.Core as Agn

#Set up the game
dice=Agn.StandardDice("dice")
while True:
    dice.roll()
    face1=dice.get_visible_side()
    print(f"Player 1 get a {face1.name}")
    dice.roll()
    face2=dice.get_visible_side()
    print(f"Player 2 get a {face2.name}")
    if face1.value==face2.value:
        print("The players are tied !")
    else:
        print(f"{"Player 1 won" if face1.value>face2.value else "Player 2 won"}")
    rep = input("Quit (y/n)? ") 
    if rep=="y":
        break

print("Thank you for playing this game !")