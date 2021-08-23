class Employee:
    no_of_leaves=8
    var=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"name is {self.name} salary is {self.salary} role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("great shit fam "+string)
class Player:
    no_of_games=4
    var=10
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"name is {self.name} game is {self.game}"

class Coolprogamer(Player,Employee):    #order of parameters is important here
    language="C++"
    def printlang(self):
        print(self.language)
u=Employee("utkarsh",30000,"sde")
v=Employee("vaibhav",20000,"sde(trainee)")
j=Player("jaadu",["volleyball"])
m=Coolprogamer("mohit",["basketball"])
#det=(m.printdetails())
#m.printlang()
#print(det)
print(m.var)