print("For square press 2 ,for cube press three")
choice=int(input("Enter your choice : "))
if choice==2:
    number=int(input("Enter Number : "))
    print(f"Square={number*number}")
elif choice==3:
    number=int(input("Enter Number : "))
    print(f"Square={number*number*number}")
else:
    print("Invalid Choice ")