#!/usr/bin/node

function converter (base) {
  return function (value) {
    return value.toString(base);
  };
}

module.exports = { converter };
