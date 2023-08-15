#!/usr/bin/node
const fs = require('fs').promises;

const fileA = process.argv[2];
const fileB = process.argv[3];
const dist = process.argv[4];

(async function () {
  const dataA = await fs.readFile(fileA);
  const dataB = await fs.readFile(fileB);
  const data = dataA + dataB;
  await fs.writeFile(dist, data);
})();
