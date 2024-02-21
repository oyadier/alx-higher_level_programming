#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }

  // Print file to console
  console.log(data);
});
