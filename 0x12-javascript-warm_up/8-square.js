#!/usr/bin/node
/*
 * square
 */
const { argv } = require('node:process');
const size = parseInt(argv[2]);
let i = 0;
if (!isNaN(size)) {
  while (i < size) {
    let row = '';
    let j = 0;
    while (j < size) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
} else { console.log('Missing size'); }
