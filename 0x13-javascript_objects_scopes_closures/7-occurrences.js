#!/usr/bin/node
/*
 * checks number of occurence of an item in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const len = list.length;
  for (let i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
