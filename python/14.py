a=int(input("enter a number"))
b,c,sum=0,1,0
print(f"Fibonacci Series of {a} numbers: ",end="")
for i in range(a):
    sum=b+c
    print(f"{b} ",end="")
    b,c=c,sum