from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
# N중 3개 고르는 방법의 수
l = list(combinations(cards, 3))

max = 0
for i in l:
  s = sum(i)
  if s <= M and s > max:
    max = s
print(max)