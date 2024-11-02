num=[]
pos=[]
neg=[]
n=int(input("size "))
for i in range(0,n):
    v=int(input("values "))
    num.append(v)
print(num)
for j in range(0,n):
    if num[j]>=0:
        pos.append(num[j])
    else:
        neg.append(num[j])
print(pos)
print(neg)
