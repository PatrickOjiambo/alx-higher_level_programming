#!/usr/bin/node
const argv = process.argv;
let value = argv[2];
let output = "";
if (isNaN(argv[2]) || argv.length < 3) {
  console.log("Missing size");
} else {
  for (let i = 0; i < value; i++) {
    for (let j = 0; j < value; j++) {
      output += "X";
    }
    console.log(output);
    output = "";
  }
}
