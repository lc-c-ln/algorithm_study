from collections import deque
T = int(input())
M, N, K = list(map(int, input().split()))
# 유기농 배추
matrix = [[0 for i in range(N)] for i in range(M)]
startPoints = []
for i in range(K):
    X, Y = list(map(int, input().split()))
    matrix[X][Y] = 1
    startPoints.append([X,Y])
for i in matrix :
    print(i)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0

while startPoints :
    while True :
        X,Y = startPoints.pop()
        if matrix[X][Y] != 0 :
            break;
    q = deque([X,Y])
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = dx + x
            ny = dy + y
            if nx
