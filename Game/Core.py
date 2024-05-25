from .Tools import Tools

class Face():
    def __init__(self, name):
        self.name=name

class Faces(Tools):
    def __init__(self, faces):
        self.faces=faces
        self.visible_face=None

    def draw_lots(self):
        self.visible_face=self.random(self.faces)
        return self
    
    def get_visible_face(self):
        return self.visible_face

class Coin():
    def __init__(self, name=None, face1=None, face2=None):
        self.name=name
        self.faces=Faces([face1,face2])

    def flip(self):
        self.faces.draw_lots()
        return self

    def get_visible_face(self):
        return self.faces.get_visible_face()

class Player():
    def __init__(self, name):
        self.name=name
        self.score=0

    def get_name(self):
        return self.name

    def set_score(self,value):
        self.score=value
        return self
    
    def increase_score(self,value):
        self.score+=value
        return self

    def get_score(self):
        return self.score

class Game(Tools):
    def __init__(self, name):
        self.name=name
        self.nb_rounds=1
        self.players=[]
        self.active_player=None
        self.max_rounds=1
        
    def add_player(self,player):
        self.players.append(player)

    def get_player(self,number):
        nb_elts=len(self.players)
        if number<1 or number>nb_elts:
            self.error(message=f"Player {number} not found")
        else:
            return self.players[number-1]
        
    def next(self):
        self.nb_rounds+=1

    def get_curr_round(self):
        return self.nb_rounds
    
    def set_max_rounds(self,number):
        self.max_rounds=number
        return self

    def get_max_rounds(self):
        return self.max_rounds

    def is_last_round(self):
        return self.get_curr_round()==self.get_max_rounds()

    def set_active_player(self,player):
        self.active_player=player

    def get_active_player(self):
        return(self.active_player)
    
    def get_players(self):
        return self.players
    
    def map_players(self,callback):
        self.my_map(self.players,callback)

    def get_winners(self):
        score=-1
        winners=[]
        for index, player in enumerate(self.players):
            if player.score>score:
                winners=[player]
                score=player.score
            elif player.score==score:
                winners.append(player)
        return winners