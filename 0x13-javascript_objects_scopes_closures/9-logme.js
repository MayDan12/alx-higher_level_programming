#!/usr/bin/node
let nargs = 0;

exports.logMe = function (item) {
  console.log(nargs + ': ' + item);
  nargs++;
};
