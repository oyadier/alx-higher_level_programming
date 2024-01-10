#!/usr/bin/node
exports.esrever = function (list) {
  const rever = [];
  let pos = 0;
  for (let x = list.length - 1; x >= 0; x--) {
    rever[pos] = list[x];
    pos++;
  }
  return (rever);
};
