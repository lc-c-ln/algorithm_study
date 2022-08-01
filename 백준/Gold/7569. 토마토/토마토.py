from collections import deque
def solution() :
    M, N, H = list(map(int, input().split()))
    total = M * N * H
    cnt = 0

    box = [[] for i in range(H)]

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    q = deque()
    ans = 0

    for i in range(H):
        for j in range(N):
            newLine = list(map(int, input().split()))
            for k in range(M):
                if newLine[k] == 1:
                    q.append([k, j, i, 0])
                    cnt += 1
                elif newLine[k] == -1:
                    cnt += 1
            box[i].append(newLine)
    if cnt == total:
        return 0
    # x,y,z,count 의 queue를 이용한다.
    while len(q) != 0:
        x, y, z, day = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx >= 0 and ny >= 0 and nz >= 0 and nx < M and ny < N and nz < H:
                if box[nz][ny][nx] == 0:
                    q.append([nx, ny, nz, day + 1])
                    box[nz][ny][nx] = 1
                    ans = max(ans, day + 1)
                    cnt += 1

    if cnt != total:
        return -1
    else:
        return ans

print(solution())






