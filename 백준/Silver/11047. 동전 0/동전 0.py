n,k = map(int,input().split())
# 그리디,
cnt = 0
val=[]
for i in range(n):
    val.append(int(input()))
for i in reversed(sorted(val)) :
    if i <= k :
        cnt += k // i
        k = k % i
# while k != 0 :
#     for i in reversed(val) :
#         if i <= k :
#             k -= i
#             break
#     cnt += 1
print(cnt)