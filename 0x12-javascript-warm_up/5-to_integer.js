#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Not a number');
} else if (isNaN(process.argv[2]) === false) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else if (typeof process.argv[2] === 'string') {
  console.log('Not a number');
}
