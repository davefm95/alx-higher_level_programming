#!/usr/bin/node
const argv = process.argv;
let j;
let numarr;
let firsth;
let secondh;
let idx = 0;
if (argv.length < 4) {
  console.log(0);
} else {
  numarr = argv.slice(2, argv.length);
  firsth = +numarr[0];
  for (j = 1; j < numarr.length; j++) {
    if (+numarr[j] > firsth) {
      firsth = +numarr[j];
      idx = j;
    }
  }
  secondh = 0;
  for (j = 0; j < numarr.length; j++) {
    if (idx === j) {
      continue;
    }
    if (+numarr[j] > secondh) {
      secondh = +numarr[j];
    }
  }
  console.log(secondh);
}
