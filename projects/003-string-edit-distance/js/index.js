const prompt = require('prompt-sync')();

const calculateEditDostance = (firstString, secondString) => {
    const emptyArr = [];

    if (firstString === secondString) {
        return 0;
    }

    for (let i = 0; i < firstString.length; i++) {
        if (
            firstString[i] !== secondString[i] &&
            firstString.length >= secondString.length
        ) {
            emptyArr.push(i);
        }
    }

    for (let j = 0; j < secondString.length; j++) {
        if (
            firstString[j] !== secondString[j] &&
            firstString.length < secondString.length
        ) {
            emptyArr.push(j);
        }
    }
    return emptyArr.length;
};

const firstString = prompt('Enter something');
const secondString = prompt('Enter something');
console.log(
    ` The edit distance between the two strings is equal to: ${calculateEditDostance(
        firstString,
        secondString
    )}`
);

// if (firstString === secondString) {
//     console.log(0); // caso base
// }
// for (let i = 0; i < firstString.length; i++) {
//     if (
//         firstString[i] !== secondString[i] &&
//         firstString.length >= secondString.length
//     ) {
//         emptyArr.push(i);
//     }
// }

// for (let j = 0; j < secondString.length; j++) {
//     if (
//         firstString[j] !== secondString[j] &&
//         firstString.length < secondString.length
//     ) {
//         emptyArr.push(j);
//     }
// }

// // console.log(emptyArr);
// console.log(emptyArr.length);
