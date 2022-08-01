from collections import deque
def solution(n, quests):
    ans = []
    a = {i:[] for i in range(1,n+1)} # k하려면, v해야한다.
    indegree = [0 for i in range(0,n)] # idx+1 하려면, ind[idx] ==0 이어야 한다.
    for i in quests:
        a[i[0]].append(i[1])
        indegree[i[1]-1] += 1
    q = deque([])

    for i in range(len(indegree)) :
        if indegree[i] == 0 :
            q.append(i+1)
    while q:
        n = q.popleft()
        for i in a[n]:
            indegree[i-1] -= 1
            if indegree[i-1] == 0:
                q.append(i)
        print(n)
solution(5, [[1, 3], [1, 4], [3, 5], [5, 4]])
