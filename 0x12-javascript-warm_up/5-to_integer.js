#!/usr/bin/node
let input = process.argv[2];
if (typeof Number(input) === 'number' && !isNaN(Number(input))) {
  console.log(`My number: ${input}`)
}else {
  console.log('Not a number');
} 
