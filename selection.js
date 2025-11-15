function selectionSort(arr) {

    let n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        let min=i
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        }
        if(min!==i){
            // Swap arr[i] and arr[min]
            let temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    };

return arr;


}

console.log(selectionSort([64, 34, 25, 12, 22, 11, 90]));