array=[1,2,1,3,2,1]
def number(num,array):
    cnt=0
    for i in array:
        if i==num:
            cnt+=1
    return cnt
print(number(1,array))

