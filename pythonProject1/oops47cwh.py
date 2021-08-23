class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f"{fname}{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property       #property decorator (this decorator is used or encapsulation)
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email not set"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter       #setter
    def email(self,string):
        print("setting now")
        names=string.split("@")
        self.fname=names[0].split(".")[0]
        self.lname=names[0].split(".")[1]
    @email.deleter      #deleter
    def email(self):
        self.fname=None
        self.lname=None
emp1=Employee("Utkarsh","Saxena")
emp2=Employee("Vaibhav","Mishra")
#print(emp1.explain())
#print(emp2.email())
#print(emp1.email)
emp2.fname="Sakshi"
print(emp2.email())   #it will not print as contructor is initialised with previous details as it is run when object is created
print(emp2.email)
emp2.email="goli.sakshi@gamail.com"
print(emp2.fname)
print(emp2.email)
del emp2.email      #works only deleteter is present
print(emp2.email)