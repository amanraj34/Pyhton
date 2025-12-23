print("To count digit in number, give any number.")
number =int(input())
count=0
rev_number=0
while number!=0:
    rev_number=rev_number*10+number%10
    number=number//10
    count=count+1
print(f"Number of digit in given number is {count}" )