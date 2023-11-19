const prompt = require('prompt-sync')({sigint: true});

function sum(numbers) {
 
  if (!numbers.length) {
    return "0.0";
  }
  else if (numbers.length === 1) {
    return numbers[0];
  }
 
  return numbers.pop() + sum(numbers);
}

const numbers = [];

while (true) {
    const number = Number(prompt("Enter a nummer (press Enter to exit): "));
    numbers.push(number);

    if (number == "") {
        numbers.pop(); // remove the last element as it is read as number 0
        break;
    }
}

console.log(sum(numbers));