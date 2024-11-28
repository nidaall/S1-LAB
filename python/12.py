a=input("Enter a string: ")
str=list(a)
str[0],str[len(str)-1]=str[len(str)-1],str[0]
for i in str:
    print(i,end="") 

    #hehe