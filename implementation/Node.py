class Node:

    def __init__(self,id,x,y,z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.in_ = dict()
        self.out_ = dict()

    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

    def getx(self):
        return self.x

    def setx(self,x):
        self.x = x

    def gety(self):
        return self.y

    def sety(self,y):
        self.y = y

    def getz(self):
        return self.z

    def setz(self,z):
        self.z = z