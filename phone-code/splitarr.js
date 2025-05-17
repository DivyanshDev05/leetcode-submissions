const rl = require('readline');

const r1 = rl.createInterface({
	input: process.stdin,
	output: process.stdout
});

r1.question("enter the arr?  ", (a) =>{
	let c = validSplitCount(a);
	console.log('valid split count');
	console.log(c);

	r1.close();
});

function validSplitCount(a){
	const b = a.split(",").map(Number);
	const s = b.reduce(sum, function (i){
		sum += i;

	}, 0);
return b;

}
