#!/usr/bin/node
const index = process.argv;
let lop = 0;
if (index.length < 3) {
  console.log('Missing number of occurrences');
} else if (index.length < 1) {
  console.log('');
} else {
  while (lop < index[2]) {
    console.log('C is fun');
    lop++;
  }
}
