from collections import deque

def solution() :
    N = int(input())
    mx = []
    for i in range(N):
        mx.append(list(map(int, list(input()))))
    answer = 0
    alist = []
    visited = [[0 for i in range(N)] for i in range(N)]

    def bfs(x,y):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        cnt = 0
        queue = deque([(x,y)])
        while len(queue) != 0 :
            x,y = queue.popleft()
            cnt += 1
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx >= N or nx <0 or ny>=N or ny<0 :
                    pass
                else :
                    # 일단 한점에서 1이고, 방문 안했어. 그럼 둘러봐야 하는데, 0이고 방문 안했어. 여긴 찍었다. 1이고 방문했다. 0이고 방문했다.
                    if mx[nx][ny] == 1 and visited[nx][ny] == 0 :
                        queue.append((nx,ny))
                        visited[nx][ny] = 1
        return cnt
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == 0 :
                visited[i][j] = 1
                if mx[i][j] != 0 :
                    answer += 1
                    alist.append(bfs(i,j))

    print(answer)
    for i in sorted(alist) :
        print(i)
solution()

