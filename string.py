str1=input("Enter a string:")
print("Original string:",str1)
char=str1[0]
length=len(str1)
str1=str1.replace(char,'$')
str1=char+str1[1:]
print("Replaced string:",str1)
