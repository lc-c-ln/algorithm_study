from collections import deque

F, S, G, U, D = list(map(int,input().split()))

visited = [-1 for i in range(F+1)]
q = deque([S])
visited[S] = 0
ans = -1

while q :
  n = q.popleft()
  if n == G :
    ans = visited[n]
    break;
  if n+U <= F and visited[n+U] == -1 :
    q.append(n+U)    
    visited[n+U] = visited[n]+1
  if n-D >= 1 and visited[n-D] == -1 :
    q.append(n-D)    
    visited[n-D] = visited[n]+1
if ans == -1 :
  print("use the stairs")
else :
  print(ans)
