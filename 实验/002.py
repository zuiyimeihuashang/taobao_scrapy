a,b = map(int,input().split())
list1=[]
for i in range(a):
    list1.append(list(map(int,input().split())))
sum = 0
try:
    for i in range(1,b+1):
        cnt =0
        for j in range(a):
            if list1[j][0] > list1[j][-1]:
                cnt += list1[j].pop(-1)
            else:
                cnt += list1[j].pop(0)
        # print("cnt:",cnt)
        sum += cnt * (2**i)
finally:
    print(sum)