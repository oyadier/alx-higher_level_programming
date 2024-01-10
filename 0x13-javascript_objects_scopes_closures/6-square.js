#!/usr/bin/node
const Sq = require('./5-square');
class Square extends Sq {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      let str = '';
      for (let y = 0; y < this.width; y++) {
        str += c;
      }
      console.log(str);
    }
  }
}
module.exports = Square;
