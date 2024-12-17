#!/usr/bin/node
/*
 * addition function
 */
const { argv } = require('node:process');
function add (a, b) {
  a = parseInt(argv[2]);
  b = parseInt(argv[3]);
  const sum = a + b;
  console.log(sum);
} add();
