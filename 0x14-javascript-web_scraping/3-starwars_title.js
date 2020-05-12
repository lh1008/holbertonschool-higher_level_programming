#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url.concat(process.argv[2]), function (err, res, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
