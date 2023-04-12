#!/usr/bin/node
const argv = process.argv;
if (argv.length < 3) { console.log('No argument'); } else if (argv.length === 3) { console.log('Argumemt found'); } else { console.log('Arguments found'); }
