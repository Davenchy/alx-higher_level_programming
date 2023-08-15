#!/usr/bin/node

function nbOccurences (list, searchElement) {
  return list.filter(x => x === searchElement).length;
}

module.exports = { nbOccurences };
