#!/usr/bin/node
const index = process.argv;
let lop = 0;
let x = 0;
if (index.length < 3 || !isNaN(typeof (Number(index[2])))) {
  console.log('Missing size');
} else if (index.lengh < 1) {
  console.log('');
} else {
  while (lop < index[2]) {
    let sq = '';
    for (x; x < index[2]; x++) {
      sq += 'x';
    }
    console.log(sq);
    x = 0;
    lop++;
  }
}
