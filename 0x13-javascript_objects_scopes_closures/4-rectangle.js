#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ch;
    let i;
    let j;
    for (i = 0; i < this.height; i++) {
      ch = '';
      for (j = 0; j < this.width; j++) {
        ch += 'X';
      }
      console.log(ch);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
