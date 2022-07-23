from collections import deque

N, K = list(map(int, input().split()))

visited = [0 for _ in range((2 * K) +1)]
q = deque([[N,0]])
ans = 0
if N >= K :
    print(N-K)
else :
    while q:
        n, cnt = q.popleft()
        if n == K :
            ans = cnt
            print(cnt)
            break;
        if n + 1 <= 2 * K and visited[n+1] == 0 :
            q.append([n + 1, cnt+1])
            visited[n+1] = 1
        if n-1 > 0 and n - 1 <= 2 * K and visited[n - 1] == 0 :
            q.append([n - 1, cnt + 1])
            visited[n - 1] = 1
        if n <= K and visited[n * 2] == 0 :
            q.append([n * 2, cnt + 1])
            visited[n * 2] = 1
