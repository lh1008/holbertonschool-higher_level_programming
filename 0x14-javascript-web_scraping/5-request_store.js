#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
	console.log(err);
      }
    });
  }
});
