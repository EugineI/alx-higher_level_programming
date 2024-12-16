#!/usr/bin/node
/*
 * arguments
 */
const { argv } = require('node:process');
const argc = argv.length - 2;
if (argc < 1) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else { console.log('Arguments found'); }
