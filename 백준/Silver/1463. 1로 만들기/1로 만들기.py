x = int(input())
memo = [x for i in range(x+1)]
memo[x] = 0
for n in reversed(range(1, x+1)):
    if n % 3 == 0:
        memo[int(n / 3)] = min(memo[n] + 1, memo[int(n / 3)])
    if n % 2 == 0:
        memo[int(n / 2)] = min(memo[n] + 1, memo[int(n / 2)])
    memo[n-1] = min(memo[n-1], memo[n] + 1)
print(memo[1])