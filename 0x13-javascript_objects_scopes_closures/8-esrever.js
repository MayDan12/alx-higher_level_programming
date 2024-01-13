#!/usr/bin/node
exports.esrever = function (list) {
  let lens = list.length - 1;
  let g = 0;
  while (lens - g > 0) {
    const aux = list[lens];
    list[lens] = list[g];
    list[g] = aux;
    g++;
    lens--;
  }
  return list;
};
