function solution(q1, q2) {
    sumQ1 = q1.reduce((sum, currVal)=>{
        return sum + currVal
    },0)
    sumQ2 = q2.reduce((sum, currVal)=>{
        return sum + currVal
    },0)
    
    q = q1.concat(q2)
    p1 = 0
    p2 = q1.length
    for (let i=0; i <= q.length * 4; i++) {
        if (sumQ1 === sumQ2) {
            return i
        } else if (sumQ1 > sumQ2) {
            sumQ1 -= q[p1]
            sumQ2 += q[p1]
            p1 += 1
        } else {
            sumQ1 += q[p2]
            sumQ2 -= q[p2]
            if (p2 == q.length) 
                p2 = 0
            else
            p2 += 1
        }
    }
    return -1;
}