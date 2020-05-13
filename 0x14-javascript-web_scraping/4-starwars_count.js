#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    let c = 0;
    for (let movie = 0; movie < json.count; movie++) {
      if (json.results[movie].characters[18]) {
        c += 1;
      }
    }
    console.log(c);
  }
});
