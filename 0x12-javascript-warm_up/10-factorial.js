#!/usr/bin/node
const argv = process.argv;
let value = argv[2];
let value2 = parseInt(value);
let result = 0;
if (isNaN(value) || value === 1) {
  result = 1;
} else {
  result = factorial(value2);
  console.log(result);
}
function factorial(value) {
  if (value > 1) {
    return value * factorial(value - 1);
  } else {
    return 1;
  }
}
