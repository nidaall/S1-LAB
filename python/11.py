a=int(input("Enter first number"))
b=int(input("Enter second number"))

for i in range(min(a,b),0,-1):
    if(a%i==0 and b%i==0):
        print(f"GCD of {a},{b} is {i}")
        break
    