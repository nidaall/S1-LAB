a=int(input("enter the limit"))

for i in range(a):
    for j in range(i):
        print("* ",end="")
    print("")

for i in range(a):
    for j in range(a-i):
        print("* ",end="")
    print("")
          