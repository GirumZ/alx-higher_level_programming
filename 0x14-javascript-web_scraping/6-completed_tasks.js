#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const resp = {};
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        if (resp[data[i].userId] === undefined) {
          resp[data[i].userId] = 0;
        }
        resp[data[i].userId]++;
      }
    }
    console.log(resp);
  }
});
