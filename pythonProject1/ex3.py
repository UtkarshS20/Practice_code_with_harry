n=18
b=9
print("total guesses=9")
while(b>=1):
    a = int(input("enter no "))
    b=b-1
    if a == n:
        print("victory. guesses taken=", 9 - b)
        break
    elif a>n:
        print("guess lower")
    elif a<n:
        print("guess higher")

    print("guesses left", b)
    if (b==0):
        print("game over")