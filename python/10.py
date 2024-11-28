import math
a=int(input("Enter coifficient a:"))
b=int(input("Enter coifficient b:"))
c=int(input("Enter coifficient c:"))
temp=b**2-4*a*c
if temp<0:
    print("No real solution")
elif temp==0:
    result=-b/(2*a)
    print("Solution is:",result)
else:
    result1=(-b+math.sqrt(temp))/(2*a)
    result2=(-b-math.sqrt(temp))/(2*a)
    print("Solution are:",result1," ",result2)