n=int(input("enter a number:"))
fib=0
n1,n2=0,1
if n<=0:
    print("enter a +ve number")
elif n==1:
    print(n1)
else:
    print("fibinacci series of ",n," is : ",n1,n2,end=" ")
    for i in range(n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3 ,end=" ")
