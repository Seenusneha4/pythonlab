s=input("Enter a string:")
count=0
for i in range(len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='1' or s[i]=='0' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=="I" or s[i]=='O' or s[i]=='U':
       count+=1
print("The number of vowels in",s,"is",count)
