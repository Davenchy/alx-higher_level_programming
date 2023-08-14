#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (x) {
  for (let i = 0; i < x; i++) {
    let line = '';
    for (let j = 0; j < x; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
