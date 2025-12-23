number=int(input("Enter a Number : "))
rev_num=0

while number!=0:
    rev_num=rev_num*10+number%10
    number=number//10
   
print(f"After reversing number is : {rev_num}")
