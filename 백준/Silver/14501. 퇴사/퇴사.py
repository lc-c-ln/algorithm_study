N = int(input())
list = []
for i in range(N):
    T, P = map(int, input().split())
    list.append([T, P])


# 마지막 날에 일하는 경우
def foo(nowDay, nowP):
    if (nowDay >= N):
        return nowP
    requiredDay, p = list[nowDay]
    a = 0
    if nowDay + requiredDay <= N :
        a = foo(nowDay + requiredDay, p + nowP)
    b = foo(nowDay + 1, nowP)
    return max(a, b)

print(foo(0, 0))