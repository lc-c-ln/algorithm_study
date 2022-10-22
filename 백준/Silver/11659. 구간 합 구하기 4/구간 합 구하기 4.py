import sys
input = sys.stdin.readline

N,M = map(int,input().split())

arr  =list(map(int,input().split()))

psum = [0]
t = 0
for i in range(N):
    t += arr[i]
    psum.append(t)

for a in range(M):
    i,j = list(map(int,input().split()))
    print(psum[j] - psum[i-1])
