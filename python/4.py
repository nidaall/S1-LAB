a,b=map(int, input("enter the two numbers:").split())
c= int(input(" \n1.Addition \n2.Subtraction \n3.Multiplication \n4.division \nEnter the choice:"))
if c==1:
    print("the sum is :",a+b)
elif c==2:
    print("the difference is :",a-b)
elif c==3:
    print("the product is :",a*b)
elif c==4:
    print("the division is :",a/b)
else :
    print("enter valid digit")
