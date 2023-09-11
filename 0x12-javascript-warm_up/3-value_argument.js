#!/usr/bin/node
const argv = process.argv
if (argv.length < 3)
{
    console.log("No arguments")
}
else{
    console.log(argv[2])
}