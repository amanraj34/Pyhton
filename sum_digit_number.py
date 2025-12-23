number=int(input("Enter a number : "))
sum=10
while number!=0:
    sum=sum+number%10
    number=number//10
print(f"Sum of digit ={sum} ")