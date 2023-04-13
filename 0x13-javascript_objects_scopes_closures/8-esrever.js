#!/usr/bin/node
exports.esrever = function (list) {
    let mid = list.length / 2;
    let i;
    for (i = 0; i < mid; i++) {
	let temp = list[i];
	list[i] = list[list.length - 1 - i];
	list[list.length - 1 - i] = temp;
    }
    return list;
};
