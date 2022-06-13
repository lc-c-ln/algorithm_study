from collections import deque


def solution(grid, k):
    answer = -1
    # 1. bfs
    # 2. dp 각 지점에 도착하는 최대 속도
    # 하루에 k칸 이동 평지or 숲 야영은 평지에서만, k가 남은 시점에서 만난 마지막 평지에서 야영
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q.append([0, 0, k, 0, 0, 0, []])
    visited = [[0 for i in range(len(grid[0]))] for _ in range(len(grid))]
    print(visited)
    print(grid)
    # 야영을 하면, visited 채우기
    while q:
        x, y, nk, cnt, px, py, v = q.popleft()
        if x == len(grid) and y == len(grid[0]):
            return cnt
        if nk == 0:  # 남은 움직임 수가 0이면
            if grid[x][y] == 'F':  # 숲이면, 가장 가까웠던 평지로 이동
                q.append([px, py, k, cnt + 1, px, py, []])
                for i in v:
                    visited[i[0]][i[1]] = 0
                continue
            else:  # p이면 그냥 야영
                nk = k
                cnt = cnt + 1
                for i in v:
                    visited[i[0]][i[1]] = 1
                v = []
                # 그동안 밟은 위치들 1로, 그 동안 밟은 위치는 parameter로 ?
        print(visited)
        print(grid)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and visited[nx][ny] == 0:
                nv = v
                nv.append([nx, ny])
                if grid[nx][ny] == 'F':
                    visited[nx][ny] = 2
                    q.append([nx, ny, k - 1, cnt, px, py, nv])
                elif grid[nx][ny] == '.':
                    visited[nx][ny] = 2
                    q.append([nx, ny, k - 1, cnt, nx, ny, nv])
    return answer
solution(
[".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"], 6)