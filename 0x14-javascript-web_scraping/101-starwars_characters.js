#!/usr/bin/node

const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api';
const filmId = process.argv[2];

function getUserName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, _, body) => {
      if (error) reject(error);
      resolve(JSON.parse(body).name);
    });
  });
}

request(`${BASE_URL}/films/${filmId}`, (error, _, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }

  const data = JSON.parse(body);
  Promise.all(
    data
      .characters
      .map(getUserName))
    .then((names) => names.forEach(name => console.log(name)));
});
