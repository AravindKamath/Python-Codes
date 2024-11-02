n=int(input("enter number of terms "))
n1,n2=0,1
count=0
if n<0:
    print("negative sequence does not exist ")
elif n==1:
    print("sequence upto ",n,"terms=",n1)
else:
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
