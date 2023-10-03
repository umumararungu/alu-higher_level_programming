#!/usr/bin/node
const file= require ('file');
const finput = "written by me";
const path = process.argv[2];
file.writeFile(path, 'utf-8', finput, (error) => {
    if (error) {
        console.error(error);
    }
    else{
        console.log('already changed');
    }

});