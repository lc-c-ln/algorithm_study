# Len = 1에서 부터, case 1. 최 우측 값만, case2. 최 우측값 + 이전 값, case 3. 모두 비포함으로 나누어 경우에 따라 max값을 변경했습니다.
# 확인할 index만 옮겨가며, max값을 계산하기에  
# 시간 복잡도는 O(n) 입니다.
def sol(nums) :
  ex = 0
  l = 0
  m = 0
  start = 0
  end = 0
  while l < len(nums) :
      s = max(ex + nums[l], 0) #
      ex = s
      if m < s :
          m = s
          if s == nums[l] :
              start = l
              end = l
          elif s == 0 :
              continue

          else :
              end = l
      l += 1
  return nums[start:end+1], m

print(
  sol([1]),
  sol([1, -2, -1, 4]),
  sol([-2,1,-3,4,-1,2,1,-5,4]),
  sol([-1])
)
