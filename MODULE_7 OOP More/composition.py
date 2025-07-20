#kind of inheritance 
#inheritance a parent class theke child class ney ar composition a 
#child class theke parent class attribute akare ney
class Engine:
    def __init__(self):
        pass
    def start(self):
        print('Engine starting')
class Driver:
    def __init__(self):
        pass

class car:
    def __init__(self):
        self.engine=Engine()
        self.driver=Driver()
    def start(self):
        self.engine.start()
gari=car()
gari.start()