#!/usr/bin/node

const request = require('request');
const baseUrl = process.argv[2];
const userId = 18;

request(baseUrl, (error, _, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }

  const data = JSON.parse(body);
  const count = data.results
    .map((f) => f.characters)
    .filter((c) => c.some(c => c.includes(userId))).length;
  console.log(count);
});
