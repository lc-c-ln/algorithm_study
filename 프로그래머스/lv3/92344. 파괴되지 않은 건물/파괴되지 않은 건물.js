// BruteForce Algorithm
// function solution(board, skill) {
//     var answer = 0;
//     cnt = 0
//     for (s of skill) {
//         for (let i = s[1]; i<=s[3]; i++) {
//             for (let j = s[2]; j <=s[4]; j++) {
//                 next = board[i][j]
//                 if (s[0]==1) {
//                     board[i][j] -= s[5]
//                 } else {
//                     board[i][j] += s[5]                                        
//                 }
//                 if (next * board[i][j] < 0) {
                    
//                 } 
//             }
//         }
//     }   
//     return cnt;
// }

function solution(board, skills) {
    let cnt = 0
    const sumMat = Array.from(Array(board.length+1), ()=> Array(board[0].length+1).fill(0))
    for (skill of skills) {
        if(skill[0]==1) { //1이면 공격임.
            sumMat[skill[1]][skill[2]] -= skill[5]            
            sumMat[skill[1]][skill[4]+1] += skill[5]
            sumMat[skill[3]+1][skill[2]] += skill[5]            
            sumMat[skill[3]+1][skill[4]+1] -= skill[5]
        } else {
            sumMat[skill[1]][skill[2]] += skill[5]
            sumMat[skill[1]][skill[4]+1] -= skill[5]
            sumMat[skill[3]+1][skill[2]] -= skill[5]            
            sumMat[skill[3]+1][skill[4]+1] += skill[5]
        }
    }
    
    const psum = Array.from(Array(board.length+2), ()=> Array(board[0].length+2).fill(0))
    // 이제, 위의 sumMat으로 부분합 알고리즘을 돌리면 된다.
    for (let i=1; i<sumMat.length; i++) {
        for (let j=1; j< sumMat[0].length; j++) {
            psum[i][j] = psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1]  + sumMat[i-1][j-1]              
        }
    }
    // 시작 board랑 합치기
    for (let i=0; i<board.length; i++) {
        for (let j=0; j< board[0].length; j++) {
            if (board[i][j] + psum[i+1][j+1] > 0) 
                cnt += 1
        }
    }
    return cnt
}
        