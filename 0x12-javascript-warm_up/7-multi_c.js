#!/usr/bin/node
const index = process.argv;
let lop = 0;
if (index.length < 3) {
  console.log('Missing number of occurrences');
} else {
  while (lop < index[2]) {
    console.log('C is fun');
    lop++;
  }
}
