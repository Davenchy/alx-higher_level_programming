#!/usr/bin/node
const dict = require('./101-data').dict;
const data = {};

for (const id of Object.keys(dict)) {
  const oc = dict[id];

  if (!data[oc]) {
    data[oc] = [];
  }

  data[oc].push(id);
}

console.log(data);
