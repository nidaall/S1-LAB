# 1
# 2 4
# 3 6 9
# 4 8 12 16

a=int(input("enter the limit"))

for i in range(1,a+1):
    for j in range(1,i+1):
        print(f"{i*j} ",end="")
    print("")