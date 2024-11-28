str=input("Enter a string: ")
dict={}
# malayalam
for i in str:
    count=0
    for j in str:
        if j==i:
            count=count+1
            dict[i]=count
for i in dict:
    print(i,"=",dict[i])
    