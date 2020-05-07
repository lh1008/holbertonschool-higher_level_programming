#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < parseInt(process.argv[2]); count++) {
    console.log('C is fun');
  }
}
