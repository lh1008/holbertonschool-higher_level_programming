#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  list.sort();
  let move = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      move += 1;
    }
  }
  return move;
};
