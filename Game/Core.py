import random

class GameElement():
    def __init__(self, name):
        self.name=name
        self.value=0

    def set_value(self,value):
        self.value=value
        return self
    
    def set_name(self,value):
        self.value=value
        return self

    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value

class GameElements():
    def __init__(self, name):
        self.name=name
        self.elements=[]

    def add(self,element):
        self.elements.append(element)

    def draw_lots(self):
        nb_elts=len(self.elements)
        if nb_elts==0:
            return None
        random_int = random.randint(0, nb_elts-1)
        return(self.elements[random_int])

    def map_on(self,callback):
        for index, element in enumerate(self.elements):
            callback(index, element)

    def get_by_number(self,number):
        if number<1 or number>len(self.elements):
            return None
        else:
            return self.elements[number-1]

    def get_elements(self):
        return self.elements

class Face(GameElement):
    def __init__(self, name):
        super().__init__(name)

class Faces(GameElements):
    def __init__(self, name):
        super().__init__(name)
        self.visible_face=None

    def draw_lots(self):
        self.visible_face=super().draw_lots()
        return self
    
    def get_visible_face(self):
        return self.visible_face

class TwoFacesObject(Faces):
    def __init__(self, name=None, face1=None, face2=None):
        super().__init__(name)
        self.name=name
        self.add(face1)
        self.add(face2)

    def flip(self):
        self.draw_lots()
        return self

class Coin(TwoFacesObject):
    def __init__(self, name=None, face1=None, face2=None):
        super().__init__(name, face1, face2)

class Card(TwoFacesObject):
    def __init__(self, name=None, face1=None, face2=None):
        super().__init__(name, face1, face2)

class StandardDeck52Cards(GameElements):
    def __init__(self, name=None):
        super().__init__(name)
        sequence=[ f"{i}" for i in range(1,11)] + ["jack", "queen", "king"]
        colours=["spades", "hearts", "clubs", "diamonds"]
        for colour in colours:
            for card in sequence:
                name=f"{card} of {colour}"
                self.add(Card(name,Face("back"),Face(name)))

class Dice(Faces):
    def __init__(self, name=None):
        super().__init__(name)
        self.name=name

    def roll(self):
        self.draw_lots()
        return self

class StandardDice(Dice):
    def __init__(self, name):
        super().__init__(name)
        face_name=["one","two","three","four","five","six"]
        for value, face in enumerate(face_name):
            self.add(Face(face).set_value(value+1))

class Player(GameElement):
    def __init__(self, name):
        super().__init__(name)

    def set_score(self,value):
        self.set_value(value)
        return self
    
    def increase_score(self,value):
        self.set_value(self.get_value()+1)
        return self

    def get_score(self):
        return self.get_value()
         
class Players(GameElements):
    def __init__(self, name):
        super().__init__(name)

class Game():
    def __init__(self, name):
        self.name=name
        self.nb_rounds=1
        self.players=Players(name)
        self.active_player=None
        self.max_rounds=1
        
    def add_player(self,player):
        self.players.add(player)

    def get_player(self,number):
        return self.players.get_by_number(number)
        
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
        self.players.map_on(callback)

    def get_winners(self):
        score=-1
        winners=[]
        for player in self.players.get_elements():
            if player.get_score()>score:
                winners=[player]
                score=player.get_score()
            elif player.get_score()==score:
                winners.append(player)
        return winners