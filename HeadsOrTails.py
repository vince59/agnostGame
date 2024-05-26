import Game.Core as Core

# Set up the game
game=Core.Game("Heads or tails")
game.set_max_rounds(4)
coin=Core.Coin("coin",Core.Face("Heads"),Core.Face("Tails"))
for p in range(1,3):
    #game.add_player(Core.Player(input(f"Player {p} name :")))
    game.add_player(Core.Player(f"Player {p}"))

while True:
    print(f"Round #{game.get_curr_round()}/{game.get_max_rounds()}")
    if game.get_curr_round() % 2:
        game.set_active_player(game.get_player(1))
    else:
        game.set_active_player(game.get_player(2))

    # Let player chose
    #face = input(f"{game.get_active_player().get_name()}, your choice ... (h) heads or (t) tails (q) Quit ? ") 
    face = "h"
    if face=="q":
        break
    chosen_face = Core.Face("Heads") if face=="h" else Core.Face("Tails")
    
    # Let chance decide
    visible_side=coin.flip().get_visible_face()
    print(f"Your choice : {chosen_face.name}")
    print(f"The side  : {visible_side.name}")
    if visible_side.name==chosen_face.name:
        print("You won !")
        game.get_active_player().increase_score(1)
    else:
        print("You lose ...")

    # Displays scores
    game.map_players(lambda idx,player: print(f"Player {player.get_name()} score = {player.get_score()}"))

    if game.is_last_round():
        break
    game.next()

winners=game.get_winners()
if len(winners)>1:
    print("You are tied!")
else:
    print(f"{winners[0].get_name()} won the game !")

print("Thank you for playing this game !")