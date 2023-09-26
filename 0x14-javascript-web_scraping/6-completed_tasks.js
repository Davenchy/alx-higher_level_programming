#!/usr/bin/node

const request = require('request');
const baseUrl = process.argv[2];

request(baseUrl, (error, _, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }

  const data = JSON.parse(body);
  const users = {};

  for (const task of data) {
    if (!task.completed) continue;
    const userId = task.userId;

    if (!users[userId]) users[userId] = 0;
    users[userId]++;
  }

  console.log(users);
});
