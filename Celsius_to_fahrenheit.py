print("for celsius to pahrenheit press 1")
print("for pahrenheitto celsiud press 2")
choice=int(input("enter your choice= "))
if choice==1:
    celsius=int(input("enter the value of celsius= "))
    pahrenheit=((9*celsius)/5)+32
    print(f"value in pahrenheit = {pahrenheit}")
elif choice==2:
    pahrenheit=int(input("enter the value of pahrenheit = "))
    celsius=(pahrenheit-32)*5/9
    print(f"value in celsius = {celsius}")
else:
    print("Invalid Choice !")