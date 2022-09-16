function solution(n)
{
    ans = 0
    for (i of String(n)) {
        ans += parseInt(i)
    }
    return ans
}