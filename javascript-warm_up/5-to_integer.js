#!/usr/bin/node
const arg1 = parseInt(process.argv[1]);
if (typeof arg1 == number){
    console.log('My number: ' + arg1);

}
else{
    console.log('Not a number');
}
