function merge(arr, low, mid, high) {
  let temp = [];
  let i = low;
  let j = mid + 1;

  // Merge two sorted halves
  while (i <= mid && j <= high) {
    if (arr[i] <= arr[j]) {
      temp.push(arr[i]);
      i++;
    } else {
      temp.push(arr[j]);
      j++;
    }
  }

  // Copy remaining left half
  while (i <= mid) {
    temp.push(arr[i]);
    i++;
  }

  // Copy remaining right half
  while (j <= high) {
    temp.push(arr[j]);
    j++;
  }

  // Put temp back into original array
  for (let k = 0; k < temp.length; k++) {
    arr[low + k] = temp[k];
  }
}

function mergeSort(arr, low, high) {
  if (low >= high) return;

  let mid = Math.floor((low + high) / 2);

  mergeSort(arr, low, mid);       // left half
  mergeSort(arr, mid + 1, high); 
  console.log(arr) // right half
  merge(arr, low, mid, high);     // merge
}

// ------- Test -------
let a = [15, 5, 24, 8, 3, 16, 10, 20];
mergeSort(a, 0, a.length - 1);
console.log(a);
