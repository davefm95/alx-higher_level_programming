#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) { return 1; } else { return n * factorial(n - 1); }
}
const argv = process.argv;
if (isNaN(+argv[2])) { console.log(1); } else { console.log(factorial(+argv[2])); }
