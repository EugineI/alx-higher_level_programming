#!/usr/bin/node
/*
 * Square inheriting from rectangle
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const size = this.height;
    const chr = c || 'X';
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += chr;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
