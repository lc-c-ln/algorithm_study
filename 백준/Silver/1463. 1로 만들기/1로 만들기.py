# x에 사용할 수 있는 연산은 3가지
n = int(input())
a = [0 for _ in range(n+1)]

for i in reversed(range(1, n)) :
  m = a[i+1]
  if i * 3 <= n:
    m = min(a[i*3], m)
  if i * 2 <= n :
    m = min(a[i*2], m)
  a[i] = m + 1
print(a[1])