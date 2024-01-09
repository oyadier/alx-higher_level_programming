#!/usr/bin/node
const index = process.argv[2];
let lop = 0;
let x = 0;
if (isNaN(index)) {
  console.log('Missing size');
} else {
  while (lop < index) {
    let sq = '';
    for (x; x < index; x++) {
      sq += 'X';
    }
    console.log(sq);
    x = 0;
    lop++;
  }
}
