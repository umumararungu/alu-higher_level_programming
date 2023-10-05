#!/usr/bin/node

const req = require('request');

const filePath = process.argv[2];
const content = process.argv[3];

req.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
