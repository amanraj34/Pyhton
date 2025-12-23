number=int(input("Enter any number to check it divisible by 5 and 11 or not!\n -> : "))
if number%5==0 and number%11 == 0:
    print("This number is divisible by 5 and 11")
else:
    print("this is not divisible by 5 and 11 ")
print("yes" if number%5==0 and number%11==0 else "no")