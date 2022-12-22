function solution(info, edges) {
    edgeArray = Array.from(Array(info.length), () =>Array())
    for (i of edges) {
        edgeArray[i[0]].push(i[1])
    }
    
    let ans = 0
    function dfs(s,w,pos, toVisit) {
        
        if (info[pos])
            w++;
        else 
            s++;
        ans = Math.max(ans, s)
        if (s <= w) 
            return
        
        let currentPos = toVisit.indexOf(pos)
        /**
            toVisit.splice(currentPos, 1)
            let newVisit = [...toVisit]
            
        */
        // 위와 아래의 두 줄의 차이가 뭐지..?
        let newVisit = [...toVisit]
        newVisit.splice(currentPos, 1)
        // 
        newVisit.push(...edgeArray[pos])

        for (let next of newVisit) {
            dfs(s, w, next, newVisit)
        }
    }
    dfs(0, 0, 0,[0])
    return ans
}