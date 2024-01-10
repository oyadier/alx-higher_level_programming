#!/usr/bin/node
const Sq = require('./5-square');
class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        let str = '';
        for (let y = 0; y < this.width; y++) {
          str += 'C';
        }
        console.log(str);
      }
    }
  }
}
module.exports = Square;
