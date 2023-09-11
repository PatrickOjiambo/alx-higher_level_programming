#!/usr/bin/node
const argv = process.argv;
let value = argv[2];
if (argv.length < 3) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < value; i++) {
    console.log("C is fun");
  }
}
