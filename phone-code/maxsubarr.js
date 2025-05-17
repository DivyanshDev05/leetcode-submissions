function getMaxSubArray(subarr){
	subarr = subarr.split(',').map(Number);
	let maxSub = subarr[0];
	let currS = 0;

	for(i=0; i<subarr.length; i++){
		if(currS<0) {
			currS = 0;
		}
		currS += subarr[i];
		console.log("CurrS: "+currS);
		maxSub = Math.max(currS, maxSub);
		console.log("MaxSub: "+maxSub);
	}

	return maxSub;
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the subarr: ', (arr) => {
	subarr = getMaxSubArray(arr);
    console.log(`Subarr: ${subarr}`);
    rl.close();
});
