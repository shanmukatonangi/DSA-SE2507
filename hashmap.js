function buildHashMap(arr){
    let map={};
    for(let i=0;i<arr.length;i++){
        map[arr[i]]=i
    }
    return map
}

function searchHashmap(map,target){
    if(target in map){
        return map[target];

    }
    return -1


}



let arr=[12,45,13,67,89,90]
let map=buildHashMap(arr)
// map={ '12': 0, '13': 2, '45': 1, '67': 3, '89': 4, '90': 5 }

console.log(searchHashmap(map,89))
