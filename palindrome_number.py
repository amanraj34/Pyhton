print("To check number is palindrome or not give any number.")
number =int(input())
orignal_number=number
rev_number=0
while number!=0:
    rev_number=rev_number*10+number%10
    number=number//10
print("Given Number is Palindrome" if orignal_number==rev_number else "Given Number is not a Palindrome" )