function solution(survey, choices) {
    var answer = '';
    const a = {
        "R" :0,
        "T" :0,
        "C" :0,
        "F" :0,
        "J" :0,
        "M" :0,
        "A" :0,
        "N" :0        
    }
    // survey에 있는 값 다 넣기
    for (let i = 0; i<choices.length; i++) {
        if (choices[i] === 1) {
            a[survey[i][0]] += 3 
        }
        else if (choices[i] === 2) {
            a[survey[i][0]] += 2 
        }
        else if (choices[i] === 3) {
            a[survey[i][0]] += 1 
        }
        else if (choices[i] === 5) {
            a[survey[i][1]] += 1 
        }
        else if (choices[i] === 6) {
            a[survey[i][1]] += 2
        }
        else if (choices[i] === 7) {
            a[survey[i][1]] += 3 
        }
    }
    ans = ""
    if (a["R"] >= a["T"])
        ans += "R"
    else 
        ans += "T"
    if (a["C"] >= a["F"])
        ans += "C"
    else 
        ans += "F"
    if (a["J"] >= a["M"])
        ans += "J"
    else 
        ans += "M"
    if (a["A"] >= a["N"])
        ans += "A"
    else 
        ans += "N"
    
    return ans;
}