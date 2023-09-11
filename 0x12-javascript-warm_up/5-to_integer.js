#!/usr/bin/node
const argv = process.argv;

const myval = parseInt(argv[2]);
if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number ${myval}`);
}
