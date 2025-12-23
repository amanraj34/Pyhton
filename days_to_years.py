Totaldays=int(input("Enter the value of day= "))
years=Totaldays//365
months=(Totaldays-years*365)//30
RemainingDay=(Totaldays-years*365-months*30)
print(f"Years= {years}")
print(f"Month= {months}")
print(f"Days= {RemainingDay}")