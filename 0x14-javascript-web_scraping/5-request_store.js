#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const baseUrl = process.argv[2];
const filename = process.argv[3];

request(baseUrl, (error, _, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }

  fs.writeFile(filename, body, (err) => {
    if (err) console.log(err);
  });
});
