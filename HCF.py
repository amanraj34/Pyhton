a= int(input("Enter First number : "))
b= int(input("Enter second number : "))
while b!=0:
    a,b=b,a%b
print(f"HCF = {a}")