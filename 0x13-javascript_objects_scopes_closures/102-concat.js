#!/usr/bin/node
const fs = require('fs');

const gf = fs.readFileSync(process.argv[2]).toString();
const gs = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], gf + gs);
