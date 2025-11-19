function BinarySearch(arr,target){
    let left=0;
    let right=arr.length-1;
    while(left<=right){
        let mid=Math.floor((left+right)/2)
        if(arr[mid]>target){
            right=mid-1
        }else if(arr[mid]<target){
            left=mid+1
        }else if(arr[mid]==target){
            return mid
        }
    }
    return -1

}


console.log(BinarySearch([12,34,54,56,67,68,99,100,101,120],101))