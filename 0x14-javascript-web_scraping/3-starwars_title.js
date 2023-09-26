#!/usr/bin/node

const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api';
const filmId = process.argv[2];

request(`${BASE_URL}/films/${filmId}`, (error, _, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }

  const data = JSON.parse(body);
  console.log(data.title);
});
