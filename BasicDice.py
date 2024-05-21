import AgnostGame.Core as Agn

#Set up the game
dice=Agn.StandardDice("dice")
while True:
    face1=dice.roll().get_visible_side()
    print(f"Player 1 get a {face1.name}")
    
    face2=dice.roll().get_visible_side()
    print(f"Player 2 get a {face2.name}")

    if face1.value==face2.value:
        print("The players are tied !")
    else:
        print(f"{"Player 1 won" if face1.value>face2.value else "Player 2 won"}")
    rep = input("Continue (y/n)? ") 
    if rep=="n":
        break

print("Thank you for playing this game !")