function solution(n, k) {
    ans = 0
    // 1. n을 k진수로 변환
    knum = ''
    while (n>0) {
        knum = n % k + knum
        n = parseInt(n / k)
    }
    
    nums = knum.split('0')
    for (num of nums) {
        // 2. num이 소수인지 판별
        if (num > 1) {
            a = 2
            flag = 0
            while (a <= Math.floor(Math.sqrt(num))) {
                if (num % a == 0) {
                    flag = 1
                    break;
                }
                a++;
            }
            if (!flag)
                ans += 1
        }
    }
    return ans;
}