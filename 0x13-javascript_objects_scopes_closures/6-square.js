#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let output = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          output = output + c;
        }
        console.log(output);
        output = '';
      }
    }
  }
};
