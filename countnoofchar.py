dict={}
str1=input("Enter a string:")
for n in str1:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
       
for k,v in dict.items():
        print("Character frequency")
        print(k,v)
