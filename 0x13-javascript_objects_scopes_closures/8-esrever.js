#!/usr/bin/node

function esrever (list) {
  if (!list.length) {
    return [];
  }

  const newlist = [];

  for (let i = list.length - 1; i >= 0; i--) {
    newlist.push(list[i]);
  }

  return newlist;
}

module.exports = { esrever };
