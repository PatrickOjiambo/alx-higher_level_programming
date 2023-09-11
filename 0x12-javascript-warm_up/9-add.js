#!/usr/bin/node
const argv = process.argv;
let value1 = argv[2];
let value2 = argv[3];

function add(a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return parseInt(a) + parseInt(b);
}
console.log(add(value1, value2));
