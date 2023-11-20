const prompt = require('prompt-sync')({sigint: true});

function calcEditDistance(string1, string2) {

    // Base case
    let substitutionCost;
    if (string1.length === 0) return string2.length;
    else if (string2.length === 0) return string1.length;
    else substitutionCost = 0;

    // Recursive part
    if (string1.at(-1) !== string2.at(-1)) {
        substitutionCost = 1;
    }

    const d1 = calcEditDistance(string1.slice(0, -1), string2) + 1;
    const d2 = calcEditDistance(string1, string2.slice(0, -1)) + 1;
    const d3 = calcEditDistance(string1.slice(0, -1), string2.slice(0, -1)) + substitutionCost;

    return Math.min(d1, d2, d3);
}

const string1 = prompt("Enter first string: ").toUpperCase();
const string2 = prompt("Enter second string: ").toUpperCase();

console.log(`Edit distance : ${calcEditDistance(string1, string2)}`);