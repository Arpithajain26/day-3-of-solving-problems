

mpp = {}

n=int(input("enter the size"))
name=input("enter the name: ")
for i in range(len(name)):
    mpp[name[i]]=mpp.get(name[i],0)+1
q=int(input("enter the num value: "))
for _ in range(q):
    a=input("enter the char: ")
    print(mpp.get(a,0))
    # get method used here to return the frequency if a exist otherwise to return 0
