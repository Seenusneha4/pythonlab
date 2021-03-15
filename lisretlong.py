lis=input("Enter a list with some strings(space separated):")
word_lis=lis.split()
word_len=[]
for n in word_lis:
    word_len.append((len(n),n))
    print(word_len)
    word_len.sort()
    print(word_len)
    print("Longest word:",word_len[-1][1])
