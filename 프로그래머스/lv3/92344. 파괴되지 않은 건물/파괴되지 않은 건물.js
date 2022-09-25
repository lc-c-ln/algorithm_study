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

// 부분합 알고리즘
function solution(board, skill) {
    let answer = 0
    const sumMat = Array(board.length+1).fill(Array(board[0].length+1).fill(0))

    // 부분합 표 완성     
    for (s of skill) {
        let [type, r1,c1, r2,c2, degree] = [...s]
        if (type == 1)
            degree *= -1
        sumMat[r1][c1] += degree
        sumMat[r2+1][c1] -= degree
        sumMat[r1][c2+1] -= degree
        sumMat[r2+1][c2+1] += degree
        console.log(sumMat, type, r1,c1,r2,c2,degree)
}

    console.log(sumMat)
    for (let i=0; i<board.length; i++) {
        for (let j=0; j<board[0].length; j++) {
            sumMat[i+1][j+1] = sumMat[i+1][j+1] + sumMat[i][j+1] +sumMat[i+1][j] -sumMat[i][j]
        }   
    }
    for (let i=0; i<board.length; i++) {
        for (let j=0; j<board[0].length; j++) {
            if(board[i][j] + sumMat[i+1][j+1] >0){
                answer++;
            }   
        }
        }
    return answer
}