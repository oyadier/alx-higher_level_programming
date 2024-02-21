#!/usr/bin/node
const fs = require('fs');
const input = process.argv[3];
const fileName = process.argv[2];

fs.writeFile(fileName, input, (err) => {
  // printing error the console
  if (err) throw err;
});
