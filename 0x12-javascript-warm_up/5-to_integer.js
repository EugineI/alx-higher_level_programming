#!/usr/bin/node
/*
 *checks if argument can be converted to integer
 */
const { argv } = require('node:process');
const test = parseInt(argv[2]);
if (!isNaN(test)) {
  console.log('My number:',test);
} else { console.log('Not a number'); }
