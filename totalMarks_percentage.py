print("Maximmum marks in each subject is 100 . ")
math=int(input("Enter marks you get in Math : "))
english=int(input("Enter marks you get in English : "))
science=int(input("Enter marks you get in Science : "))
hindi=int(input("Enter marks you get in Hindi : "))
SocialScience=int(input("Enter marks you get in Social Science : "))
MaximumMarks=500
totalMarks=math+english+science+hindi+SocialScience
totalPercentage=(totalMarks/MaximumMarks)*100
print(f"Total Percentage = {totalPercentage}")