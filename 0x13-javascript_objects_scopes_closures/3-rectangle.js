#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w < 0 || h < 0 || w === 0 || h === 0 || typeof w === 'undefined' || typeof h === 'undefined') {
      module.exports = class Rectangle {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let move = 0; move < this.height; move++) {
      console.log('X'.repeat(this.width));
    }
  }
};
