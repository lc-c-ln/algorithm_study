N = int(input())
rgb = []
for i in range(N):
    rgb.append(list(map(int, input().split())))

ans = [rgb[0]]
for i in range(1,N) :
    a0 = min(ans[i-1][2], ans[i-1][1]) + rgb[i][0]
    a1 = min(ans[i-1][0], ans[i-1][2]) + rgb[i][1]
    a2 = min(ans[i-1][0], ans[i-1][1]) + rgb[i][2]
    ans.append([a0,a1,a2])
# print(ans)
print(min(ans[N-1]))