#!/usr/bin/node

const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api';
const userId = 18;

request(`${BASE_URL}/people/${userId}`, (error, _, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }

  const data = JSON.parse(body);
  console.log(data.films.length);
});
