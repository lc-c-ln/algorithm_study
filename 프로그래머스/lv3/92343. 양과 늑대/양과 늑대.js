// function solution(info, edges) {
//     edgeDict = {}
//     for (i of edges) {
//         if (i[0] in edgeDict) 
//             edgeDict[i[0]].push(i[1])
//         else edgeDict[i[0]] = [i[1]]
//     }    
//     var answer = 0
//     function dfs(s, w, pos, toVisit) { // 양과 늑대, 현재 위치, 방문 예정인 노드들
//         let newToVisit = [...toVisit]
//         if (info[pos])
//             w ++;
//         else 
//             s ++;
//         answer = Math.max(answer, s)
        
//         if (s <= w) 
//             return
        
//         if (!(pos in edgeDict)){
//             return
//         }
//         // toVisit에 현재 pos에서 갈 수 있는 노드들 모두 추가
//         newToVisit.push(...edgeDict[pos])
//         newToVisit = newToVisit.filter((node)=> node !== pos)
//         for (const i of toVisit){
//             dfs(s, w, i, newToVisit)
//         }
//     }
    
//     dfs(0,0,0,[0]);
//     return answer;
// }

function solution(info, edges) {
  let answer = 0;
  let connectedNode = Array.from({ length: info.length }, () => []);

  for (let i = 0; i < edges.length; i++) {
    let current = edges[i];
    connectedNode[current[0]].push(current[1]); // connectedNode에 연결된 노드를 인덱스에 맞게 push
  }

  function dfs(currentNode, sheep, wolf, possible) {
    let newPossibles = [...possible];
    let currentIndex = newPossibles.indexOf(currentNode);

    if (info[currentNode]) {
      wolf++;
    } else {
      sheep++;
    }

    answer = Math.max(answer, sheep); // sheep의 수를 매 경우마다 answer와 비교하여 최대 값을 저장

    if (sheep === wolf) {
      // 양의 수인 sheep과 wolf의 수가 같은 경우
      return;
    }

    newPossibles.push(...connectedNode[currentNode]);
    // connectedNode에 현재 노드에서 이동 가능한 노드를 newPossibles에 추가
    newPossibles.splice(currentIndex, 1);

    for (const nextNode of newPossibles) {
      dfs(nextNode, sheep, wolf, newPossibles);
    }
  }

  dfs(0, 0, 0, [0]); // DFS를 사용해 모든 경로를 탐색

  return answer; // 모든 경로를 탐색후 최대 값인 answer를 반환
}