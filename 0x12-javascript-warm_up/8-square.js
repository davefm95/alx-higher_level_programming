#!/usr/bin/node
const argv = process.argv;
let i;
let j;
let sqChar;
if (isNaN(+argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < (+argv[2]); i++) {
    sqChar = '';
    for (j = 0; j < (+argv[2]); j++) { sqChar += 'X'; }
    console.log(sqChar);
  }
}
