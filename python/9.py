year=int(input("enter a year:"))
if(year%100!=0):
    if(year%4==0):
        print("Leap year")
    else:
        print("not a Leap year")
else:
    if(year%400==0):
        print("Leap year")
    else:
        print("Not a Leap year")