function solution(alp, cop, problems) {
    time = 0
    algo = 0
    coding = 0
    
    maxA = 0
    maxC = 0
    for (let i of problems) {
        maxA = Math.max(i[0], maxA)
        maxC = Math.max(i[1], maxC)
    }
    
    if (maxA < alp && maxC< cop) {
        return 0
    }
    if(alp >= maxA) {
        alp = maxA
    }
    if(cop >= maxC) {
        cop = maxC
    }        
    
    dp = new Array(maxA)
    for (let i = 0; i< maxA+2; i++) {
        dp[i] = new Array(maxC+2).fill(302)
    }
    dp[alp][cop] = 0
    
    
    for (let i = alp; i<=maxA; i++) {
        for (let j=cop; j<= maxC; j++) {
        dp[i+1][j] = Math.min(dp[i+1][j], dp[i][j] +1)
        dp[i][j+1] = Math.min(dp[i][j+1], dp[i][j] +1)
        
        for (let p of problems) {
            if(i>=p[0]&& j>=p[1]){
                if(i+p[2]>maxA&&j+p[3]>maxC){
                    dp[maxA][maxC]=Math.min(dp[maxA][maxC], dp[i][j]+p[4]);
                }
                else if(i+p[2]>maxA){
                    dp[maxA][j+p[3]]=Math.min(dp[maxA][j+p[3]],dp[i][j]+p[4]);
                }
                else if(j+p[3]>maxC){
                    dp[i+p[2]][maxC]=Math.min(dp[i+p[2]][maxC],dp[i][j]+p[4]);
                }
                else if(i+p[2]<=maxA && j+p[3]<=maxC){
                    dp[i+p[2]][j+p[3]]=Math.min(dp[i+p[2]][j+p[3]],dp[i][j]+p[4]); 
                }
            }}
    }
    }
    
    return dp[maxA][maxC];
}

