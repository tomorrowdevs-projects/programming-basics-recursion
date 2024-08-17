const prompt = require('prompt-sync')();

/**
 *
 * @param {Number} userNumber - The non-negative decimal number to be converted to binary:
 * @returns {String} - A string representing the binary equivalent of the supplied decimal number:
 */
const decimalToBinary = (userNumber) => {
    return userNumber === 0 || userNumber === 1
        ? userNumber.toString()
        : decimalToBinary(Math.trunc(userNumber / 2)) +
              (userNumber % 2).toString();
}; // For numbers greater than 1, it recursively calls the function by dividing by 2 and adds the remainder of the division by 2 to the end of the resulting string.

const userNumber = Number(prompt('Enter a non-negative integer'));
if (userNumber < 0) {
    console.log('Enter a non-negative integer');
} else {
    console.log(
        `The binary equivalent of the non-negative decimal number entered by the user is: ${decimalToBinary(
            userNumber
        )}`
    );
}
