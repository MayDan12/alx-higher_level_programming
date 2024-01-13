#!/usr/bin/node
function factorial (u) {
  if (u < 0) {
    return (-1);
  }
  if (u === 0 || isNaN(u)) {
    return (1);
  }
  return (u * factorial(u - 1));
}

console.log(factorial(Number(process.argv[2])));
