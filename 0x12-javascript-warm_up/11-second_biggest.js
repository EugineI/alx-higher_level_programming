#!/usr/bin/node
/*
 * second largest number
 */
const { argv } = require('node:process');
const argc = argv.length - 2;
const args = argv.slice(2).map(Number);
if (argc <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);
  const unique = [...new Set(sorted)];
  console.log(unique[1] || 0);
}
