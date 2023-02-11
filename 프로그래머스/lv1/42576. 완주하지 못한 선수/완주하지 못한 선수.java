import java.util.Arrays;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Arrays.sort(participant);
        Arrays.sort(completion);
        int i = 0;
        int j = 0;
        boolean flag = false;
        
        while (i < participant.length && j < completion.length) {
            if (participant[i].equals(completion[j])) {
                i ++;
                j ++;
            } else {
                return participant[i];
            }
        }
        return participant[i];
    }
}