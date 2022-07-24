from collections import deque

F, S, G, U, D = list(map(int,input().split()))

visited = [0 for i in range(F+1)]
count = [0 for i in range(F+1)]

def bfs(v) :
  q = deque([v])
  visited[v] = 1
  while q :
    v = q.popleft()
    if v == G:
      return count[G]
    if v + U <= F and visited[v + U] == 0 :
      visited[v + U] = 1
      count[v+U] = count[v] + 1
      q.append(v + U)
    if v - D > 0 and visited[v - D] == 0 :
      visited[v- D] = 1
      count[v- D] = count[v] + 1
      q.append(v- D)
  if count[G] == 0 :
    return "use the stairs"

print(bfs(S))
      

  

# ans = -1


# while q :
#   v = q.popleft()
#   if pos == G :
#     # ans = count[pos]
#     break;
#   if pos + U <= F and visited[pos + U] == 0 :
#     visited[pos+U] = 1
#     q.append(pos + U)
#     count[pos+U] = count[pos] + 1
#   if pos - D > 0 and visited[pos - D] == 0 :
#     visited[pos-D] = 1
#     q.append(pos - D)
#     count[pos - D] = count[pos] + 1
# if count[G] == 0 :
#   print("use the stairs")
# else :
#   print(count[G])