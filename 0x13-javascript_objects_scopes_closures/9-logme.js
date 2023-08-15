#!/usr/bin/node

let i = 0;

function logMe (item) {
  console.log(`${i++}: ${item}`);
}

module.exports = { logMe };
