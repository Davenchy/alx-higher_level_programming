#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

request(URL, (_, res, _a) => console.log(`code: ${res.statusCode}`));
