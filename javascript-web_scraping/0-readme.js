#!/usr/bin/node
const file= require ('file') 
file.readFile('README.md', (err, inputD) => {
    if (err) throw err;
    console.log(inputD.toString());
})
