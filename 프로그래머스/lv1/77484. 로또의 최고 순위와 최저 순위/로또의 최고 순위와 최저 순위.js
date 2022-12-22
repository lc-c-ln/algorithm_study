function solution(lottos, win_nums) {
    cnt = 0
    zero = 0
    
    for (i of lottos) {
        // if (win_nums.indexOf(i)>=0) {
        if (win_nums.includes(i)) {
        
            cnt += 1
        }
        else if (i === 0)
            zero +=1
    }
    max = cnt + zero
    if (max == 0) {
        max = 1
    }
    min = cnt
    if (cnt <= 1)
        min = 1
    return [7-max, 7-min]
}