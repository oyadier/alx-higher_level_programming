#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w === 0 || h === 0 || w < 1 || h < 1 || w === undefined || h === undefined) {
      Object();
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
