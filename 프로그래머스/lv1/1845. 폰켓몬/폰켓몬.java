import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Set<Integer> targetSet = new HashSet<Integer>();
        for (int i : nums) {
            targetSet.add(i);
        }
        
        return Math.min(targetSet.size(), nums.length / 2);
    }
}