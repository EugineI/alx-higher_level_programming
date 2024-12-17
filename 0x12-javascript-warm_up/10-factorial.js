#!/usr/bin/node
/*
 * factorial
 */
const { argv } = require('node:process');
const factorial = (n) => {
  if (isNaN(n)) {
    return 1;
  }
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};
const num = parseInt(argv[2]);
console.log(factorial(num));
