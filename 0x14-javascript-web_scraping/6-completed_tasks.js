#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const info = JSON.parse(body);
    for (v in info) {
      if (info[v].completed === true) {
	console.log(info[v].userId, info[v].completed);
      }
    }
  }
});
