#!/usr/bin/node
/*
 * looping with argument
 */
const { argv } = require('node:process');
const common = 'C is fun';
let i = 0;
const test = parseInt(argv[2]);
if (!isNaN(test)) {
  while (i < test) {
    console.log(common);
    i++;
  }
} else { console.log('Missing number of occurrences'); }
