function solution(numbers) {    
    console.log("1" + undefined === undefined + "1")
    function compare(a,b) {
        if (a != undefined && b != undefined) {
            // undefined               
            return String(a) + b > b + String(a) 
        }
        return String(a) + b > b + String(a) 
    }    
    
    function merge(left,right) {
        const sortedArr = [];
        while (left.length && right.length) {
            if (compare(left[0], right[0])) {
                sortedArr.push(left.shift())
            } else {
                sortedArr.push(right.shift())                
            }
        }
        return [...sortedArr,...left,...right]
        // return sortedArr.concat(left,right)
    }
    
    function mergeSort(arr) {
        if (arr.length <= 1) return arr;
        const mid = Math.ceil(arr.length/2)
        const left = arr.slice(0,mid)
        const right = arr.slice(mid)
        return merge(mergeSort(left), mergeSort(right))
    }
    a = mergeSort(numbers)
    if (parseInt(a) == 0) {
        return "0"
    }
    else 
    
        return a.join("")
}

    
//     function merge(arr, left, mid, right) {
//         i = left; // 잘린 부분(왼쪽)
//         j = mid + 1 // 잘린 부분(오른쪽)
//         k = left; // 결과 arr index
    
//         while (i <= mid && j <= right) { // 둘 중 하나 끝날 때 까지
//             if (compare(arr[i], arr[j])) {
//                 ans[k++] = arr[i++] 
//             } else {
//                 ans[k++] = arr[j++]
//             }
//         }
    
//         if (i>mid) {
//             for (l = j; l <= right; l++) {
//                 ans[k++] = arr[l]
//             }
//         }
//         else {
//             for (l=i; l <= mid; l++) {
//                 ans[k++] = arr[l]
//             }
//         }
//         for (l=left; l<=right;l++){
//             arr[l] = ans[l]
//         }
//     }
// function merge_sort(arr, left, right) {
//     if (left < right) {
//         mid = parseInt((left + right) / 2)
//         merge_sort(merge_sort(arr, left,mid))
//         merge_sort(merge_sort(arr, mid+1, right))
//         merge(arr, left, mid, right)
//     }
// }
//     merge_sort(numbers, 0, numbers.length)
    
