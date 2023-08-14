#!/usr/bin/node
const args = process.argv;
let m = 0;
if (args.length > 3) {
  m = args.slice(2).map(i => parseInt(i)).sort((a, b) => b - a)[1];
}
console.log(m);
