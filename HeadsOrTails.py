import AgnostGame.Core as Agn

#Set up the game

face1=Agn.Element("heads") # pile
face2=Agn.Element("tails") # face
coin=Agn.Ensemble("coin")
coin.add(face1)
coin.add(face2)

while True:
    # Let the player chose
    face = input("(h) heads or (t) tails (q) Quit ? ") 
    if face=="q":
        break
    chosen_face = face1 if face=="h" else face2
    rnd_face=coin.random(2)

    print(f"Your choice : {chosen_face.get_info()["name"]}")
    print(f"The result  : {rnd_face.get_info()["name"]}")
    if rnd_face.name==chosen_face.name:
        print("You won !")
    else:
        print("You lose ...")

print("Thank you for playing this game !")