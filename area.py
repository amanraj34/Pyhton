print("if you want to find area of circle press 2 for area of rectangle press 1")

value=int((input("enter your choice= ")))
if(value==2):
    radius=int(input("Enter the value of radius= "))
    
    print(f"area of circle = {(22*radius*radius)/7}")
elif(value==1):
    length=int(input("enter the value of length= "))
    breadth=int(input("enter the value of b= "))
    print(f"area of rectangle = {(length*breadth)}")
else:
    print("invalid choice")