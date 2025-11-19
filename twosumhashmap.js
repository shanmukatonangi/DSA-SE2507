function twosum(arr,target){
    const map=new Map();

    for(let i=0;i<arr.length;i++){
        const complement=target-arr[i];
        if(map.has(complement)){
            return [map.get(complement),i]
        }
        map.set(arr[i],i)
    }
}

let arr=[1,2,3,4,5]
let target =9;
console.log(twosum(arr,target))