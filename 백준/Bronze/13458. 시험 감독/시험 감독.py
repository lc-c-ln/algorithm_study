import math

n = int(input())
arr = list(map(int,input().split()))
b, c = map(int, input().split())

cnt = 0
# if b > c :
for i in range(len(arr)):
    arr[i] -= b
cnt += len(arr)
for i in arr :
    if i <= 0 :
        continue;
    else :
        # print(i,c, math.ceil(i/c))
        cnt += math.ceil(i/c)

print(cnt)