import java.util.PriorityQueue;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> q = new PriorityQueue();
        for (int i: scoville) {
            q.add(i);
        }
        int cnt = 0;
        int a = q.poll();
        while (a < K) {
            if (q.size() < 1) {
                return -1;
            }
            cnt++;
            int b = q.poll();
            int c = a + b * 2;
            q.add(c);
            a = q.poll();
        }
        return cnt;
    }
}
//         make scoville a MinHeap
//         class MinHeap() {
//             private ArrayList<Integer> heap;
//             public void insert(int val) {
//                 this.heap.add(val);
//                 int p = this.heap.size() - 1;
//                 while (p > 1 && heap.get(p/2) > heap.get(p)) {
//                     // System.out.println("swap");
//                     int tmp = heap.get(p/2);
//                     heap.set(p/2, heap.get(p));
//                     heap.set(p, tmp);
//                 }
//             }
            
//             public int pop() {
//                 int minVal = this.heap[0];
//                 ArrayList<Integer> th = this.heap;

//                 if (th.size() - 1 < 1) {
//                     return 0;
//                 }
                
//                 th.set(1, heap.get(th.length - 1));
//                 th.remove(th.length - 1);
                
//                 int pos = 1;
//                 int min = th.get(pos);
//                 while (pos < th.size()) {
//                     int sV = th.get(pos * 2);
//                     int sP = pos*2;
//                     if (sV< th.get(pos * 2 + 1)) {
//                         sV = th.get(sP + 1);
//                         sP= sP + 1
//                     }
//                     if (min < sV) {
//                         break;
//                     }
//                     th.set(pos, sV);
//                     th.set(sP, min);
//                     pos = sP;
                                        
                    
                    
//                 }
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
//                 while ((pos * 2) < heap.size()) {
//                     int min = heap.
//                 }
//                 while ((pos * 2) < heap.size()) {
//                     int min = heap.get(pos * 2);
//                     int minPos = pos * 2;
//                 }
                
                
//                 int tmp = this.heap[this.heap.length - 1];
                
//                 this.heap[0] = tmp;
                
//                 while ()
                   
//             }
//         }
//         public void insert(int val) {
//             heap.add(val)
//         }
        
        
        
//         return answer;
//     }
// }