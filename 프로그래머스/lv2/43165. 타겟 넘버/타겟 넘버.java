import java.util.*;
class Solution {
    int cnt = 0;
    public int solution(int[] numbers, int target) {
        int answer = 0;
        dfs(numbers, 0, target);
        return cnt;
    }
        public void dfs(int[] numbers, int currentSum, int target) {            
            if (numbers.length==0) {
                if(currentSum == target) {
                    cnt ++;
                }
                return;
            }
            dfs(Arrays.copyOfRange(numbers, 1, numbers.length), currentSum + numbers[0], target);
            dfs(Arrays.copyOfRange(numbers, 1, numbers.length),currentSum - numbers[0], target);
            return;
        }

}