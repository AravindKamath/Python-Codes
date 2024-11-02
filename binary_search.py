a=[]
n=int(input("size "))
for i in range(0,n):
    v=int(input("value "))
    a.append(v)
ele=int(input("element to be searched "))
first=0
last=n-1
while first<last:
    mid=(first+last)/2
    mid=int(mid)
    if a[mid]==ele:
        print(ele," found in pos ",mid+1)
        break
    elif a[mid]<ele:
        first=mid+1
    else:
        last=mid-1
