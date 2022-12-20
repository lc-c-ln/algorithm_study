a, K = map(int,input().split())
DP = [1000000 for i in range(K+1)]
DP[a] = 0
while a <= K :
    if (a + 1 <= K) :
        DP[a + 1] = min(DP[a + 1], DP[a] + 1)
    if (a * 2 <= K):
        DP[2 * a] = min(DP[a * 2], DP[a] + 1)
    a += 1
print(DP[-1])