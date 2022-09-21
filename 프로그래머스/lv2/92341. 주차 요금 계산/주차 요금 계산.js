function solution(fees, records) {
    function calcFee(time) {
        if (fees[0] >= time) {
            return fees[1]
        } else {
            return (fees[1] + (Math.ceil( (time-fees[0])/fees[2] )*fees[3]))
        }
    }
    
    const cars = []
    const parkingLot ={}
    const totalTimes = {} 
    for (record of records) {
        const [h, m, c, io] = record.split(/ |:/)
        const t = Number(h*60) + Number(m)
        if (io === "IN") {
            parkingLot[c] = t
            if (! (c in totalTimes)) {
                totalTimes[c] = 0            
                cars.push(c)
            }
        } else { // 출차 시
            parkedTime = t - parkingLot[c]
            totalTimes[c] += parkedTime
            parkingLot[c] = -1
        }
    }
    for (key in parkingLot){
        if (parkingLot[key] !== -1) {
            totalTimes[key] += 1439 - parkingLot[key]
        }
    }
    const answer = []
    cars.sort()
    
    for (i of cars) {
        answer.push(calcFee(totalTimes[i]))
    }
    
    return answer;
}

// function solution(fees, records) {
//     function calcFee(inTime, outTime) {
//         const time = outTime - inTime
//         if (fees[0] >= time) {
//             return fees[1]
//         } else {
//             return (fees[1] + (Math.round((time-fees[0])/fees[2])*fees[3]))
//         }
//     }
    
//     const parkingLot ={}
//     const ans = {} 
//     for (record of records){
//         const [h, m, c, io] = record.split(/ |:/)
//         const t = Number(h*60) + Number(m)
//         if (io === "IN") {
//             parkingLot[c] = t
//         } else {
            
//             f = calcFee(parkingLot[c],t)
//             if (c in ans){
//                 ans[c] += f
//             } else {
//                 ans[c] = f
//             }
//             parkingLot[c] = -1
//         }
//     }
//     for (key in parkingLot){
//         console.log(key,parkingLot[key],"남은 차량")
//         if (parkingLot[key] !== -1) {
//             ans[key] += calcFee(parkingLot[key], 1439)
//         }
//     }
    
//     console.log(ans)
//     var answer = [];
//     return answer;
// }

