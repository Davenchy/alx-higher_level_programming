#!/usr/bin/node
const SuperSquare = require('./5-square');

class Square extends SuperSquare {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      let line = '';

      for (let j = 0; j < this.height; j++) {
        line += c || 'X';
      }

      console.log(line);
    }
  }
}

module.exports = Square;
