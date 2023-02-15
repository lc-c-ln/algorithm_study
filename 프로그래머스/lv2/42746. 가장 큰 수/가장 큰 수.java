import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        StringBuffer answer = new StringBuffer();
        ArrayList<String> nums = new ArrayList();
        for (int i: numbers) {
            nums.add(Integer.toString(i));
        }
        Collections.sort(nums, (o1, o2) -> {
            Integer f = Integer.parseInt(o1+o2);
            Integer s = Integer.parseInt(o2+o1);
            return s.compareTo(f);
        });
        
        for (String num: nums) {
            answer.append(num);
        }
        String ans = answer.toString();
        // print(ans.substring(0));
        
        if (ans.substring(0,1).equals("0")) {
            return "0";
        } 
                         
                         // (Integer.parseInt(o1+o2).compareTo(Integer.parseInt(o2+o1)));
        
        // Arrays.sort(numbers, 
        //     (o1, o2)-> (Integer.parseInt(Integer.toString(o1) + Integer.toString(o2)))
        //             .compareTo(Integer.parseInt(Integer.toString(o2) + Integer.toString(o1))));
        // System.out.println(ans.substring(0,1));       
        // System.out.println(numbers)     ;       
//         for (int i=0; i<numbers.length; i++) {
//             for (int j=i+1; j<numbers.length; j++) {
//                 if ()
//             }
//         }
        
        
//         HashMap<String, ArrayList<Integer>> map = new HashMap();
//         ArrayList<String> nums = new ArrayList<>();
//         for (int num: numbers) {
//             String n = Integer.toString(num);
//             char firstLetter = n.charAt(0);
//             while (n.length() < 4) {
//                 n += firstLetter;
//             }

            
//             ArrayList<Integer> sameNums = map.getOrDefault(n, new ArrayList());
//             if (sameNums.size() ==0) {
//                 nums.add(n);            
//             }
//             sameNums.add(num);
//             map.put(n, sameNums);
//         }
        
        
//         Collections.sort(nums, Comparator.reverseOrder());
//         for (String key : nums) {
//             for (int value: map.get(key)) {
//                 answer += value;
//             }
//         }
                
        return answer.toString();
    }
}