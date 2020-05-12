#!/usr/bin/node
class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let move = 0; move < this.height; move++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
