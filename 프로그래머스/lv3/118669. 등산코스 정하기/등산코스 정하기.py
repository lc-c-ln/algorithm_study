from queue import PriorityQueue
import heapq
MAX_INT = 10000001

def solution(n, paths, gates, summits):
    # 다익스트라 
    # for (i in paths)
    pathDic= {i:[] for i in range(1,n+1)}
    for p in paths :
        pathDic[p[0]].append((p[1],p[2]))
        pathDic[p[1]].append((p[0],p[2]))    
    # Queue 초기화
    intensity = [MAX_INT for i in range(n+1)]
    visited = [False for _ in range(n+1)]
    q = []
    for g in gates:
        heapq.heappush(q, (0,g))
        intensity[g] = 0
    # summit 만나면 break 해야하는데, 그러려면 가장 intensity가 작은 것들 중, 가장 summit 이 작은 것이 제일 앞에 와야한다.
    # (break 후, summit들 돌면서 확인하면 안 그래도 됨)
    while q :
        f = heapq.heappop(q)
        try :
            while (visited[f[1]]) :
                f = heapq.heappop(q)
        except :
            break
        visited[f[1]] = True
        if f[1] in summits :
            continue
        # intensity 갱신
        for [to, w] in pathDic[f[1]] :
            if not visited[to] :
                intensity[to] = min(max(w, intensity[f[1]]), intensity[to])
                heapq.heappush(q, (intensity[to], to))
                
    ans = 0
    for i in summits :
        if intensity[i] < intensity[ans]:
            ans = i
        elif intensity[i] == intensity[ans] and i < ans:
            ans = i
    return [ans, intensity[ans]]