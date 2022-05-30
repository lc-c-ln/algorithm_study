from collections import deque
N = int(input())
E = int(input())
edges = {i : [] for i in range(1,N+1)}
for i in range(E) :
    edge = list(map(int,input().split()))
    edges[edge[0]].append(edge[1])
    edges[edge[1]].append(edge[0])
queue = deque([1])
visited = [0 for i in range(N+1)]
visited[1] = 1
cnt = 0

while queue :
    v = queue.popleft()

    for i in edges[v] :
        if visited[i] == 0 :
            visited[i] = 1
            cnt += 1
            queue.append(i)

print(cnt)