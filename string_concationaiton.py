inputstring=input("input string ")
count=0
for char in inputstring:
    count=count+1
newstring=inputstring[0:2]+inputstring[count-2:count]
print("input string= "+inputstring)
print("new string= "+newstring)