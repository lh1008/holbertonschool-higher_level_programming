#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing size');
} else if (typeof process.argv[2] === 'string') {
  if (isNaN(parseInt(process.argv[2]) === false)) {
    console.log('Missing size')
  } else {
    for (let count = 0; count < parseInt(process.argv[2]); count++) {
      console.log('X'.repeat(parseInt(process.argv[2])));
    }
  }
}
  console.log(isNaN(process.argv[2]));
