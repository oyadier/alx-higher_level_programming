#!/usr/bin/node
function factorial (arg) {
  if (arg === 0 || arg === 1 || isNaN(arg)) {
    return (1);
  } else {
    return (arg * factorial(arg - 1));
  }
}
const argi = Number(process.argv[2]);
console.log(factorial(argi));
