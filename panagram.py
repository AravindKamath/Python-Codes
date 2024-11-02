string=input("string ")
string=string.lower()
allalphabets="abcdefghijklmnopqrstuvwxyz"
flag=0
for char in allalphabets:
    if char not in string.lower():
        flag=1
    else:
        flag=0
if flag == 1:
    print("It is not a panagram ")
else:
    print("It is a panagram")