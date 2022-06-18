from collections import deque
T = int(input())
for time in range(T) :
    M, N, K = list(map(int, input().split()))
    # 유기농 배추
    matrix = [[0 for i in range(N)] for i in range(M)]
    startPoints = []
    for i in range(K):
        X, Y = list(map(int, input().split()))
        matrix[X][Y] = 1
        startPoints.append([X,Y])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    cnt = 0

    while startPoints :
        go = 0
        while startPoints :
            X,Y = startPoints.pop()
            if matrix[X][Y] != 0 :
                go = 1
                break;
        if go == 1 :
            q = deque([[X,Y]])
            cnt += 1
            while q :
                x,y = q.popleft()
                for i in range(4) :
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if nx >= 0 and nx < M and ny < N and ny >=0 :
                        if matrix[nx][ny] != 0:
                            matrix[nx][ny] = 0
                            q.append([nx,ny])
    print(cnt)