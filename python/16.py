a=input("enter a string")
if (a[-3:]!=("ing")):
    b=a+"ing"
else:
    b=a+"ly"

print(b)