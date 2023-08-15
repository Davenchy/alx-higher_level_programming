#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || w <= 0 || !h || h <= 0) {
      return undefined;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    if (!this.width || !this.height) {
      return;
    }

    for (let i = 0; i < this.height; i++) {
      let line = '';

      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }

      console.log(line);
    }
  }

  rotate () {
    if (!this.width || !this.height) {
      return;
    }

    const tmp = this.width;

    this.width = this.height;
    this.height = tmp;
  }

  double () {
    if (!this.width || !this.height) {
      return;
    }

    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
