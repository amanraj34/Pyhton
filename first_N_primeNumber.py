print("To check number is prime of not, give any number : ")
number=int(input())
count=0
for i in range(1,(number//2)+1):
    if number%i==0 :
        count+=1
print("Yes It is prime number "if count<=1 else "It is not a prime number ")