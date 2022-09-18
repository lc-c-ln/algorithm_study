function solution(n) {
    var answer = 0;
    li = []
    cnt = 1
    
    while (cnt <= n) {
        if (n % cnt == 0) {
            console.log(cnt)
            answer += cnt
        }
        cnt ++
    }
    return answer;
}