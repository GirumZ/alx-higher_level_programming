#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let filmCount = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          filmCount++;
        }
      }
    }
  }
  console.log(filmCount);
});
