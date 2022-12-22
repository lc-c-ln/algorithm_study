n =int(input())
dp= [[],[0,"1"]]

for i in range(2,n+1) :
    num, nextStr = dp[i-1]
    if i % 3 == 0 :
        if num > dp[i // 3][0]:
            num, nextStr = dp[i // 3]
    if i % 2 == 0:
        if num > dp[i // 2][0]:
            num, nextStr = dp[i // 2]
    num += 1
    nextStr = str(i) + " " + nextStr
    dp.append([num, nextStr])

print(dp[n][0])
print(dp[n][1])