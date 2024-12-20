#!/usr/bin/node
/*
 * reverse the order of a list
 */
exports.esrever = function (list) {
  const newlist = [];
  const len = list.length;
  for (let i = 1; i <= len; i++) {
    newlist[i - 1] = list[len - i];
  }
  return newlist;
};
