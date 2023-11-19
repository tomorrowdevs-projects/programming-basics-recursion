const prompt = require('prompt-sync')({sigint: true});

function toBinary(decNumber) {

    if (decNumber === 0 || decNumber === 1) {
        return decNumber;
    }

    return toBinary(Math.trunc(decNumber / 2)) + "" + decNumber % 2;
}

let decimalNumber;
while (true) {
    decimalNumber = prompt("Enter a positive number: ");
 
    if (decimalNumber !== "" && decimalNumber !== " ") {
        decimalNumber = Number(decimalNumber);
    }

    if (decimalNumber >= 0 && Number.isInteger(decimalNumber)) break;

    console.log("ERROR - Insert a positive number!");
}

console.log(`Binary form: ${toBinary(decimalNumber)}`);