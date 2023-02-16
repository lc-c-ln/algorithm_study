import java.util.*;

class Solution {
    ArrayList<Integer> unvisited = new ArrayList<>();
    int l;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        l = n;
        for (int i = 0; i < n; i++) {
            unvisited.add(i);
        }
        while(unvisited.size() > 0) {
            answer++;
            // System.out.print(unvisited);
            dfs(unvisited.get(0), computers);
        }
        
        return answer;
    }
    
    public void dfs(int n, int[][] computers) {
        unvisited.remove(Integer.valueOf(n));
        for (int i=0; i < l; i++) {
            // System.out.print( unvisited.contains(i));            
            if (unvisited.contains(i) && computers[n][i] == 1) {
                // System.out.print("unvisited");            
                dfs(i,computers);                
            }
        }
        
        // for (int i: unvisited) {
        //     if (computers[n][i] == 1) {
        //     }
        // }
    }  
}