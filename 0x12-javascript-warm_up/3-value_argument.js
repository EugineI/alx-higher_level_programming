#!/usr/bin/node
/*
 * value of arguments
 */
const { argv } = require('node:process');
let argc = 0;
argv.forEach(() => {
  argc++;
});
if (argc <= 2) {
  console.log('No argument');
} else {
  argv.forEach((val, index) => {
    if (index >= 2) {
      console.log(val);
    }
  });
}
