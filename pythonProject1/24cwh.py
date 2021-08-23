#f strings
import math
me="utkarsh"
al=3
#a="this is %s %s"%(me,al)
#a="this is {1} {0}"
#b=a.format(me, al)
#print(b)
a=f"this is {me} {al} {math.cos(65)}"
print(a)