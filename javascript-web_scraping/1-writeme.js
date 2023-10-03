#!/usr/bin/node
const fs= require ('fs');
const finput = "written by me";
const path = process.argv[2];
fs.writeFile(path, 'utf-8', finput, (error) => {
    if (error) {
        console.error(error);
    }
    else{
        console.log('already changed');
    }

});