function solution(info, edges) {
    edgeDict = {}
    for (i of edges) {
        if (i[0] in edgeDict) 
            edgeDict[i[0]].push(i[1])
        else edgeDict[i[0]] = [i[1]]
    }
    distanceToSheep = Array(info.length).fill(10000)
    function getDistanceToNextSheep(pos) {
        if (info[pos] === 0) 
            return 0
        else {
            if (!(pos in edgeDict))
                return 10000
            distanceToSheep[pos] =
                Math.min(getDistanceToNextSheep(edgeDict[pos][0]),
                getDistanceToNextSheep(edgeDict[pos][1])) + 1
            return distanceToSheep[pos]
        }
    }
    let sheepCnt = 1
    let wolfCnt = 0
    let toVisit = []

    function visit(pos) {
        if (pos in edgeDict) {
            for (nextNode of edgeDict[pos]) {
                    // 현재 pos에 연결된 노드들 전부 확인
                    if (info[nextNode] === 0) {
                        sheepCnt ++;
                        visit(nextNode)
                    } else {
                        getDistanceToNextSheep(nextNode)
                        toVisit.push(nextNode)
                    }
            }
        }
    }
    visit(0)
    while (toVisit) {
        min = 10000
        next = -1
        for (i of toVisit) {
            if (distanceToSheep[i] < min){
                min = distanceToSheep[i]
                next = i
            }
        }
        if (next === -1) {
            return sheepCnt
        }
        console.log("방문 할 곳",next, "wolf", wolfCnt, "다음", distanceToSheep[next], sheepCnt)
        toVisit = toVisit.filter((e)=> e !== next )
        if (wolfCnt + distanceToSheep[next] < sheepCnt) {
            wolfCnt ++;
            visit(next)
        } else {
            return sheepCnt
        }
    }    
}