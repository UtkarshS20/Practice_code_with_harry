def getdate():
    import datetime
    return datetime.datetime.now()
def data_entry():
    a=int(input("press 1 for harry 2 for rohan 3 for hammad"))
    b=int(input("press 1 for exercise 2 for diet"))
    if a==1:
        print("you choosed harry")
        if b==1:
            add=input("what do you want to add")
            f=open("ex5harryexercise.txt","a")
            c=f.write("["+str(getdate())+"]"+add+"\n")
            print("entry done")
            f.close()
        elif b==2:
            add=input("what do you want to add")
            f=open("ex5harryfood.txt","a")
            c=f.write("["+str(getdate())+"]"+add+"\n")
            print("entry done")
            f.close()
    elif a==2:
        print("you choosed rohan")
        if b==1:
            add=input("what do you want to add")
            f=open("ex5rohanexercise.txt","a")
            c=f.write("["+str(getdate())+"]"+add+"\n")
            print("entry done")
            f.close()
        elif b==2:
            add=input("what do you want to add")
            f=open("ex5rohanfood.txt","a")
            c=f.write("["+str(getdate())+"]"+add+"\n")
            print("entry done")
            f.close()
    elif a==3:
        print("you choosed hammad")
        if b==1:
            add=input("what do you want to add")
            f=open("ex5hammadfood.txt","a")
            c=f.write("["+str(getdate())+"]"+add+"\n")
            print("entry done")
            f.close()
        elif b==2:
            add=input("what do you want to add")
            f=open("ex5hammadfood.txt","a")
            c=f.write("["+str(getdate())+"]"+add+"\n")
            print("entry done")
            f.close()
    else:
        print("please choose from 1, 2 or 3")
def retrieve():
    a = int(input("press 1 for harry 2 for rohan 3 for hammad"))
    b = int(input("press 1 for exercise 2 for diet"))
    if a==1:
        if b==1:
            f=open("ex5harryexercise.txt","rt")
            for i in (f.readlines()):
                print(i)
            f.close()
        elif b==2:
            f = open("ex5harryfood.txt", "rt")
            for i in (f.readlines()):
                print(i)
            f.close()
    elif a==2:
        if b==1:
            f=open("ex5rohanexercise.txt","rt")
            for i in (f.readlines()):
                print(i)
            f.close()
        elif b==2:
            f = open("ex5rohanfood.txt", "rt")
            for i in (f.readlines()):
                print(i)
            f.close()
    elif a==3:
        if b==1:
            f=open("ex5hammadexercise.txt","rt")
            for i in (f.readlines()):
                print(i)
            f.close()
        elif b==2:
            f = open("ex5hammadfood.txt", "rt")
            for i in (f.readlines()):
                print(i)
            f.close()
a=input("enter a to add data r to retrieve data")
if a=="a":
    data_entry()
elif a=="r":
    retrieve()
