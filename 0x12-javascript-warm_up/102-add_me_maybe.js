#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  let newNumber = number + 1;
  theFunction(newNumber);
};
