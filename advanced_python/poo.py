# Clases y objetos 

# Creación clase 
class Human:
    def __init__(self, n, o): #Constructor
        self.name = n
        self.occupation = o

    def do_work(self):
        if (self.occupation == "engineer"):
            print(self.name, "is an engineer")

        elif (self.occupation == "actor"):
            print(self.name, "is an actor")

    def speaks(self):
        print(self.name, "says, welcome to my program")

Ronald = Human("Ronald", "engineer")
Ronald.do_work()
Ronald.speaks()










