#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let f = 0; f < list.length; f++) {
    if (searchElement === list[f]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
