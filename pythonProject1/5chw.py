d1={}
d2={"abc":"123","ccd":"345","dvs":"678","ghi":{"a":"123","b":"456"}}
print(d2)
print(d2["ghi"])
print(d2["ghi"]["b"])
d2["alex"]="789"
print(d2)
d2[45]="89"
print(d2)
del d2[45]
print(d2)
d3=d2.copy()
del d3["abc"]
print(d2)
print(d3)
print(d2.get("abc"))
d2.update({"xyz":"987"})
print(d2)
print(d2.keys())
print(d2.items())

