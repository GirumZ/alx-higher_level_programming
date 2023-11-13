#!/usr/bin/node
const args = process.argv.length;
const elements = [];
if (args <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < args; i++) {
    elements.push(parseInt(process.argv[i]));
  }
  elements.sort((a, b) => b - a);
  console.log(elements[1]);
}
