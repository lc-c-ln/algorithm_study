# 14889
import itertools

n = int(input())
mat = []
nums = []
for i in range(n) :
    nums.append(i)
    mat.append(list(map(int, input().split())))
# s = 0
# for i in mat :
#     s += sum(i)
# a = s
ans = 999999
for i in list(itertools.combinations(nums, int(n/2))) :
    # combi : 팀
    cnt = 0
    n_sub_i = [x for x in nums if x not in i]
    a = list(itertools.combinations(i,2))
    for k in a :
        cnt += mat[k[0]][k[1]] + mat[k[1]][k[0]]

    b = list(itertools.combinations(n_sub_i,2))
    for k in b :
        cnt -= mat[k[0]][k[1]] + mat[k[1]][k[0]]


    if abs(cnt) < ans :
        ans = abs(cnt)
print(ans)
