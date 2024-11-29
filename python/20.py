dict={}
n=int(input("Enter a limit: "))
for i in range(1,n+1):
    val=int(input(f"Enter value{i}: "))
    dict[i]=val
keys=list(dict.keys())
vals=list(dict.values())
vals.sort()
print(vals)
for i in range(0,n):
    dict[i]=vals[i]
print(dict)
# for i,j in keys,vals:
#     dict[i]=vals[j]
# print(dict)