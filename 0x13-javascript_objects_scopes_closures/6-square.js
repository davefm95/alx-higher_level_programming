#!/usr/bin/node
const Quad = require('./5-square');
class Square extends Quad {
  charPrint (c) {
    if (typeof c !== 'undefined') {
      let ch;
      let i;
      let j;
      for (i = 0; i < this.height; i++) {
        ch = '';
        for (j = 0; j < this.width; j++) {
          ch += c;
        }
        console.log(ch);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
