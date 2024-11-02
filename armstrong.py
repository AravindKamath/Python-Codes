num=int(input("number "))
temp=num
count=0
while temp!=0:
    y=temp%10
    count=count+(y*y*y)
    temp=temp//10
if num==count:
    print(num," is armstrong")
else:
    print(num," is not armstrong")