#!/usr/bin/node
/*
 * Square inheriting from rectangle
 */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
