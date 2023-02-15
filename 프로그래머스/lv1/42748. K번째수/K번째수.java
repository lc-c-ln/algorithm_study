import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList();        
        int cnt = 0;
        int[] ans = new int[commands.length];
        for (int[] command: commands) {
            
            int i = command[0];
            int j = command[1];
            int k = command[2]; 
            List<Integer> subList = new ArrayList<>();
            for (int a: Arrays.copyOfRange(array, i-1,j)) {
                subList.add(a) ;
            }
            Collections.sort(subList);
            ans[cnt] = subList.get(k-1);
            cnt++;
        }
        return ans;
    }
}