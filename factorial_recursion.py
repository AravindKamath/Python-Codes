def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
n=int(input("number "))
if n<0:
    print("factorial of negative does not exist ")
elif n==0:
    print("factorial of ",n," = ",n)
else:
    print("factorial of ",n," = ",fact(n))