from collections import deque
N = int(input())
A,B = list(map(int,input().split()))
M = int(input())
linkedList = { i : [] for i in range(1, N+1)}
for i in range(M):
    parent, child = list(map(int, input().split()))
    linkedList[parent].append(child)
    linkedList[child].append(parent)
def bfs() :
    visited = []
    queue = deque()
    queue.append([A,0])
    while queue :
        # print(queue)
        node, cnt = queue.popleft()
        if node == B:
            return cnt
        for i in linkedList[node] :
            if i not in visited :
                queue.append([i,cnt+1])
                visited.append(i)
    return -1
print(bfs())