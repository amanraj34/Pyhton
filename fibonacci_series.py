print("To write fibinacci series give value of n term : ")
n=int(input("N =  "))
a,b=0,1
i=1
while i<=n:
    print(a,end=" ")
    a,b=b,a+b
    i+=1