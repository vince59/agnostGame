import Game.Core as Core

# Set up the game
game=Core.Game("Dice game")
game.set_max_rounds(4)
dice=Core.StandardDice("dice")
for p in range(1,3):
    #game.add_player(Core.Player(input(f"Player {p} name :")))
    game.add_player(Core.Player(f"Player {p}"))

while True:
    print(f"Round #{game.get_curr_round()}/{game.get_max_rounds()}")

    face1=dice.roll().get_visible_face()
    print(f"{game.get_player(1).get_name()} got a {face1.get_name()}")
    
    face2=dice.roll().get_visible_face()
    print(f"{game.get_player(2).get_name()} got a {face2.get_name()}")

    if face1.value==face2.value:
        print("The players are tied !")
    elif face1.value>face2.value:
        print(f"{game.get_player(1).get_name()} won")
        game.get_player(1).increase_score(1)
    else:
        print(f"{game.get_player(2).get_name()} won")
        game.get_player(2).increase_score(1)

    # Displays scores
    game.map_players(lambda idx,player: print(f"Player {player.get_name()} score = {player.get_score()}"))

    #rep = input("Continue (y/n)? ") 
    rep="y"
    if rep=="n":
        break

    if game.is_last_round():
        break
    game.next()

winners=game.get_winners()
if len(winners)>1:
    print("You are tied!")
else:
    print(f"{winners[0].get_name()} won the game !")
print("Thank you for playing this game !")