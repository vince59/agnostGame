import inspect
import json
import random

class Tools:
    def __init__(self, name):
        pass
    
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

    def random(self,elements):
        nb_elts=len(elements)
        if nb_elts==0:
            return None
        random_int = random.randint(0, nb_elts-1)
        return(elements[random_int])

    def my_map(self,elements,callback):
        for index, element in enumerate(elements):
            callback(index, element)