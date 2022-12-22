from itertools import combinations
N = int(input())

list = []
for i in range(N) :
  # N중 3개 고르는 방법의 수
  x,y = map(int, input().split())
  list.append([x,y])

for i in list :
  cnt = 1
  for j in list :
    if i[0] < j[0] and i[1] < j[1] :
      cnt += 1
  print(cnt)
