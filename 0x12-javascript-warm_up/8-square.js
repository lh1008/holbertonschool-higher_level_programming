#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing size');
} else {
  for (let count = 0; count < parseInt(process.argv[2]); count++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
