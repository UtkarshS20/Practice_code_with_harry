#f=open("utkarsh.txt","w")
#a=f.write("this is test case from write a file\n")
#print(a)
#f.close()
#f=open("utkarsh.txt","a")
#a=f.write("this is test case from write a file\n")
#print(a)
#f.close()

#handle read and write both
f=open("utkarsh.txt","r+")
print(f.read())
f.write("thanks")
