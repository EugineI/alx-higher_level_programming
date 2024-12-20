#!/usr/bin/node
/*
 * Rectangle class
 */
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const h = this.height;
    const w = this.width;
    for (let i = 0; i < h; i++) {
      let row = '';
      for (let j = 0; j < w; j++) {
        row = row + 'X';
      }
      console.log(row);
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const newH = this.height;
    const newW = this.width;
    this.width = newH;
    this.height = newW;
  }
}
module.exports = Rectangle;
