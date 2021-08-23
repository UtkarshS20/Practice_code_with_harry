a=input()
b=input()
try:
    print("the sum",
          int(a)+int(b))
except Exception as e:
    print(e)
print("must show")