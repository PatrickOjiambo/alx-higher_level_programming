#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const value of list) {
    if (value === searchElement) {
      counter = counter + 1;
    }
  }
  return counter;
};
