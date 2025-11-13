// Traditional Solution (Javascript)
// function findMaxElement(arr) {
//   let max = arr[0];
//   for (let i = 1; i < arr.length; i++) {
//     if (arr[i] > max) {
//       max = arr[i];
//     }
//   }
//   return max;
// }

// console.log(findMaxElement([3, 6, 8, 4, 5]));

// Traditional Solution (Javascript)
// function reverseArray(arr) {
//   let start = 0;
//   let end = arr.length - 1;
//   while (start < end) {
//     [arr[start], arr[end]] = [arr[end], arr[start]]; // Swap elements using destructuring assignment
//     start++;
//     end--;
//   }
//   return arr;
// }

// console.log(reverseArray([3, 6, 8, 4, 9, 5]));