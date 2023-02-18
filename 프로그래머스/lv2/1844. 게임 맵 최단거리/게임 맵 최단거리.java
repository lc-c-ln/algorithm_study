import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int[] dx = new int[] {1,0,-1,0};
        int[] dy = new int[] {0,-1,0,1};
        
        Queue<int []> q = new LinkedList();
        q.add(new int[] {0,0,0});
        while (q.size()>0) {
            int[] next = q.poll();
            int x = next[0];
            int y = next[1];
            int cnt = next[2];
//             System.out.print(x);
//             System.out.print(y);
            
            if (x == maps.length-1 && y== maps[0].length-1) {
                return cnt +1 ;
            }
            
            for (int i=0;i<4; i++) {
                int nextX = x + dx[i];
                int nextY = y + dy[i];
                if (nextX >= 0 && nextX < maps.length && nextY < maps[0].length && nextY>=0 && maps[nextX][nextY] != 0 ) {
                    maps[nextX][nextY] = 0;
                    q.add(new int[] {nextX, nextY, cnt+1});
                }
            }
        }
        return -1;
    }
}