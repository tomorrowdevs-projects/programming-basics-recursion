const prompt = require('prompt-sync')({sigint: true});

function encodeRunLength(string) {
    // Base case
    if (!string.length) return string; // return []
    // Recursive path
    let list = []; // the compressed list to be returned
    list.push([string[0]]); // insert the firs character in the list

    for (let i = 1; i <= string.length; ++i) { // use i as a counter of the same adjacent character

        if (string[i - 1] !== string[i]){ // check if two adjacent character are equals or not
            list.push(i);
            break;
        }

    }

    return [...list, ...encodeRunLength(string.slice(list.pop()))]; // here I use the last element in the list (the counter) as the index where to cut
}

const decompressedList = prompt("Enter a string: ");

console.log(`Compressed list: ${encodeRunLength(decompressedList)}`);