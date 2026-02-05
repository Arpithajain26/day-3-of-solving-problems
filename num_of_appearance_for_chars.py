s="abcshdjddcccccbb"

def charactercount(c,s):
    count=0
    for i in range(len(s)):
        if s[i]==c:
            count+=1
    return count
print(charactercount('b',s))



# another method using hashing and array
n=int(input("enter the size: "))
name=input("enter the char name: ")
hasharray=[0]*256
for ch in name:
    index=ord(ch)
    hasharray[index]+=1
q=int(input("enter the value of q: "))
for _ in range(q):
    nam=input("enter the one with which u want to count: ")
    index=ord(nam)
    print(hasharray[index])
    