function naiveSearch(text, pattern) {
const n=text.length;
const m=pattern.length;
let occurrence=[]

for(let i=0;i<=n;i++){
    let j;
    for(j=0;j<m;j++){
        if(text[i+j]!==pattern[j]){
            break;
        }
    }    if(j===m){
        occurrence.push(i);
    }
}

return occurrence;


}

console.log(naiveSearch("shanshakshan","shan"));