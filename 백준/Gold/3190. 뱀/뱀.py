from collections import deque

n = int(input())
k = int(input())

mat = [[0 for _ in range(n)]for i in range(n)]

for i in range(k):
    x,y = map(int, input().split())
    mat[x-1][y-1] = 1
l = int(input())

turnTime = {}
for i in range(l) :
    sec, dir = input().split()
    turnTime[int(sec)] = dir

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x = 0
y = 0

cnt = 0

headDir = 0
q = deque()


def turn(c) :
    global headDir
    if c == 'L':
        headDir = (headDir + 3) % 4
    else :
        headDir = (headDir + 1) % 4
q.append([0,0])

while True :
    if x >= n or x < 0 or y >= n or y < 0 or mat[x][y] == -1 :
        break;
    q.append([x, y])
    # 머리가 도착한 위치 확인 ( 사과 확인 ) - 사과없음
    if mat[x][y] == 0 :
        tailx, taily= q.popleft()
        mat[tailx][taily] = 0
    # 머리 위치 변화.

    mat[x][y] = -1
    # head 회전
    if cnt in turnTime.keys() :
        turn(turnTime[cnt])
    # 다음에 도착할 곳
    cnt += 1
    x += dx[headDir]
    y += dy[headDir]


print(cnt)

