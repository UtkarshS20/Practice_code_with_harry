class Dad:
    cricket=1
class Son(Dad):
    football=1
    def pfootball(self):
        return f"yea i play football {self.football} no. of times"
class Grandson(Son):
    football = 6
    #def pfootball(self):
    #    return f"yea i play football very good {self.football} no. of times"
asta=Dad()
yuno=Son()
sasuke=Grandson()
print(sasuke.pfootball())