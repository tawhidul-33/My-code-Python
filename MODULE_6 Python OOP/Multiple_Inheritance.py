class Family:
    def __init__(self,address):
        self.address=address
class School:
    def __init__(self,id,level):
        self.id=id
        self.level=level
class Sports:
    def __init__(self,game):
        self.game=game
class Student(Family,School,Sports):
    def __init__(self, address,id,level,game):
        super().__init__(address)#or, Family.__init__(self,address)
        School.__init__(self,id,level)
        Sports.__init__(self,game)


        