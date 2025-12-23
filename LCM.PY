print("Give two number to find its LCM")
a=int(input("A = "))
b=int(input("B = "))
max_value=max(a,b)
while True :
    if max_value%a==0 and max_value%b==0 :
        print(f"LCM = {max_value}")
        break
    max_value=max_value+1