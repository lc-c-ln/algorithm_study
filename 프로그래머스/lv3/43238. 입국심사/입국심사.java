import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        long left = times[0];
        long right = times[0] * (long) n;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            long sum = 0;
            for (int t:times) {
                sum += mid / t;
            }
            // System.out.print(mid);
            // System.out.print(" : 미드");
            // System.out.print(sum);
            // System.out.print(" : 섬");

            if (sum < n) {
                if (right - left == 1) {
                    return right;
                }
                left = mid+1;
            } else {
                right = mid-1;
                answer = mid;
            }
        }
        return answer;
    }
}