
console.log('typeof console log')
console.log(typeof typeof 100)
console.log('typeof console log')
function abc() {

console.log(abc.xyz)

}
console.log('before xyz')
abc()
abc.xyz = 400
abc.xyz = 500
console.log('after xyz')
abc()

const n = [1,2,3,4]
n[100] = 5000
console.log(n)

const p=[...'P',...['H']]
console.log(p)

console.log(parseInt('5'+3))
console.log(parseInt('10+3'))

console.log('------')
console.log('5'+3)
console.log('------')
console.log('5'-3)
console.log('------')
console.log(1 + + '5')
console.log('------')
