function solution(id_list, report, k) {
    let ids = {}
    let reportedTime = {}
    for (i of id_list) {
        ids[i] = []
        reportedTime[i] = 0
    }
    
    report = new Set(report)
    for (i of report) {
        let [reporter, reportee] = i.split(" ")
        ids[reportee].push(reporter)
    }

    for (i of Object.keys(ids)) {
        if (ids[i].length >= k){
            // console.log(i, "가 신고 많이 받았다.")
            for (j of ids[i]) {
                // console.log(i,"를 신고한",j,"가 메일을 하나 받았다.")
                reportedTime[j] += 1
            }
        }
    }    
    var answer = [];
    
    for (id of id_list) {
        answer.push(reportedTime[id])
    }
    
    return answer;
}