#!/usr/bin/node
exports.esrever = function (list) {
  const line = list;
  const line_2 = [];

  for (let i = line.length - 1; i >= 0; i--) {
    line_2.push(line[i]);
  }
  return line_2;
};
