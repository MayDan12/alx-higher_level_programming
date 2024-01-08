#!/usr/bin/node
const arg = process.argv;
if (arg.length <= 3) {
  console.log("0");
} else {
  const arr = arg.slice(2).map(Number);
  const second = arr.sort(function (a, b) {
    return b - a;
  })[1];
  console.log(second);
}
