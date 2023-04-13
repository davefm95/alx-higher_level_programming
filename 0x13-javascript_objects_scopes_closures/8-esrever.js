#!/usr/bin/node
exports.esrever = function (list) {
  const mid = list.length / 2;
  let i;
  for (i = 0; i < mid; i++) {
    const temp = list[i];
    list[i] = list[list.length - 1 - i];
    list[list.length - 1 - i] = temp;
  }
  return list;
};
