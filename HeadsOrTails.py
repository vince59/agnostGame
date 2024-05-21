import AgnostGame.Core as Agn

#Set up the game
coin=Agn.Coin("coin","heads","tails")

while True:
    # Let the player chose
    face = input("(h) heads or (t) tails (q) Quit ? ") 
    if face=="q":
        break
    chosen_face = Agn.Face("heads") if face=="h" else Agn.Face("tails")
    
    visible_side=coin.flip().get_visible_side()
    print(f"Your choice : {chosen_face.name}")
    print(f"The result  : {visible_side.name}")
    if visible_side.name==chosen_face.name:
        print("You won !")
    else:
        print("You lose ...")

print("Thank you for playing this game !")