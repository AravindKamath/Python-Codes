a=[]
n=int(input("size "))
for i in range(0,n):
    v=int(input("element "))
    a.append(v)
print("unsorted elements= ",a)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(a[j]<a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("sorted elements = ",a)
