#!/usr/bin/node
const argv = process.argv;
let i;
if (isNaN(+argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < (+argv[2]); i++) {
    console.log('C is fun');
  }
}
