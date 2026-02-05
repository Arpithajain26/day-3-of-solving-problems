n=int(input("enter the number"))
arr=list(map(int,input().split()))

hasharray=[0]*10000000
for i in range(n):
    hasharray[arr[i]]+=1
q=int(input("enter the number: "))
for _ in range(q):
    number=int(input())
    print(hasharray[number])
