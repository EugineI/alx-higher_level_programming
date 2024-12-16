#!/usr/bin/node
/*
 * concatenation
 */
const { argv } = require('node:process');
const sentence = argv[2] + ' is ' + argv[3];
console.log(sentence);
