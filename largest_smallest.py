n=int(input("number "))
large=0
small=9
while n>0:
    rem=n%10
    if small>rem:
        small=rem
    if large<rem:
        large=rem
    n=n//10
print("smallest digit ",small)
print("largest digit ",large)
