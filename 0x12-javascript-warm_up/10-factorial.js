#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a === 1 || a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(parseInt(process.argv[2])));
