a,b,c=map(int,input("enter three number:").split())

if a>b and a>c:
    print("A is largest")
elif b>c and b>a:
    print("B is largest")
else:
    print("C is largest")
