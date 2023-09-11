#!/usr/bin/node
const argv = process.argv;
if (argv.length < 4) {
  console.log("0");
} else {
  let myArr = argv.slice(2,);
  myArr.sort(function (a, b) {
    return b - a;
  });
  console.log(myArr[1])
}
