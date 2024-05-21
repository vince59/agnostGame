import json
import random
import inspect

class Element:
    def __init__(self, name):
        self.name=name
        self.value=0

    def set_value(self,value):
        self.value=value
        return self

    def get_value(self,value):
        return self.value
    
    def get_info(self):
        return ({key: value for key, value in self.__dict__.items()})

    def dump(self,file=None):
        if file==None:
            print(self.get_info())
        else:
            with open(file, 'w') as f:
                json.dump(self.get_info(), f, indent=4)

    def log(self,file=None, type="inf",message=""):
        message=f"{type}-{message}"
        if file==None:
            print(message)
        else:
            with open(file, 'a') as f:
                f.write(message)

    def error(self,file=None,message=""):
        self.log(file,"err",message)
        stack = inspect.stack()
        frame = stack[1]
        filename = frame.filename
        line = frame.lineno
        self.log(file,"err",f"File: {filename}, Ligne: {line}")
        exit()

    def warning(self,file=None,message=""):
        self.log(file,"wrn",message)

class Ensemble(Element):
    def __init__(self, name):
        super().__init__(name)
        self.elements=[]
        self.active_element=None

    def add(self,element):
        self.elements.append(element)

    def get_info(self):
        return ({**super().get_info(),**{'elements':[x.get_info() for x in self.elements]}})
        
    def random(self,number=1):
        nb_elts=len(self.elements)
        if number<1 or number>nb_elts:
            self.error(message="Value out of limit")
        random_int = random.randint(0, number-1)
        self.active_element=self.elements[random_int]
        return self.active_element

class Face(Element):
    def __init__(self, name):
        super().__init__(name)

class ThrowableSet(Ensemble):
    def __init__(self, name):
        super().__init__(name)

    def get_visible_side(self):
        return self.active_element
    
class Coin(ThrowableSet):
    def __init__(self, name,name_face1="",name_face2=""):
        super().__init__(name)
        self.add(Face(name_face1))
        self.add(Face(name_face2))

    def flip(self):
        super().random(len(self.elements))

class Dice(ThrowableSet):
    def __init__(self, name):
        super().__init__(name)

    def roll(self):
        super().random(len(self.elements))

class StandardDice(Dice):
    def __init__(self, name):
        super().__init__(name)
        face_name=["one","two","three","four","five","six"]
        for value, face in enumerate(face_name):
            self.add(Face(face).set_value(value+1))

class Player(Element):
    def __init__(self, name):
        super().__init__(name)

class Team(Ensemble):
    def __init__(self, name):
        super().__init__(name)

class Game(Ensemble):
    def __init__(self, name):
        super().__init__(name)

    
    

