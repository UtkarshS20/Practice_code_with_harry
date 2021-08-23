import random
lst=["s","w","g"]
a=0
point_c=0
point_p=0
while a<10:
    computer = random.choice(lst)
    b = input()
    if b=="s":
        if computer=="s":
            print("same,try again")
        elif computer=="w":
            point_p=point_p+1
        elif computer=="g":
            point_c=point_c + 1
    elif b=="w":
        if computer=="s":
            point_c=point_c + 1
        elif computer=="w":
            print("same,try again")
        elif computer=="g":
            point_p=point_p + 1
    elif b == "g":
        if computer == "s":
            point_p=point_p + 1
        elif computer == "w":
            point_c=point_c + 1
        elif computer == "g":
            print("same,try again")
    else:
        print("please press only s, w or g")
    a+=1
    print(computer)
if point_c>point_p:
    print("you lost.Your points=",point_p)
elif point_c<point_p:
    print("you won.Your points=",point_p)
else:
    print("draw")