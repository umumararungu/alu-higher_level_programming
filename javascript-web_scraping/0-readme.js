#!/usr/bin/node
const file= require ('file') 
file.readFile('0-readme.js', (err, inputD) => {
    if (err) throw err;
    console.log(inputD.toString());
})
