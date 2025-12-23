i=int(input("enter the frequency of number : "))
num=0
for j in range(1,i+1):
    num=num+int(input(f"enter number {j}= "))
avg=num/i
print(avg)