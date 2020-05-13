#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    let c = 0;
    for (const movie of json.results) {
      for (const character of movie.characters) {
        if (character.endsWith('/18/')) {
          c += 1;
        }
      }
    }
    console.log(c);
  }
});
