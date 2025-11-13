function finite(text,pattern){
    const n=text.length;
    const m=pattern.length;
    let occurrence=[];
    let state=0;

    for(let i=0;i<n;i++){
        if(text[i]===pattern[state]){
            state++;
            if(state===m){
                occurrence.push(i-m+1);
                state=0;
            }
    }else{
        if(text[i]===pattern[0]){
            state=1;
        }else{
            state=0;
        }
    }
}
 return occurrence;
}

console.log(finite("shanshakshan","shan"));