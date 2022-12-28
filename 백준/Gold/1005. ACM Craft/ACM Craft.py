import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def mintime(n):
    # base case
    if n not in pre : return time[n-1]
    if dp[n]!=-1 : return dp[n]
    # step
    for build in pre[n]:
        dp[n] = max(dp[n], mintime(build))
    dp[n] += time[n-1]
    return dp[n]

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    dp = [-1]*(n+1)
    pre = defaultdict(list)
    for i in range(k):
        x, y = map(int, input().split())
        pre[y].append(x)
    w = int(input())
    print(mintime(w))