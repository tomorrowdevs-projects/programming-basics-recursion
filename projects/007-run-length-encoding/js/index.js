const prompt = require('prompt-sync')();

/**
 *
 * @param {array} decompressedList
 * @returns A function that maps each individual element of the array and counts how many duplicates there are.
 */
function compressedList(decompressedList) {
    if (!decompressedList) return []; // Base case: empty array

    const compressedArray = []; // Empty array to insert each repeated element

    decompressedList.forEach(
        (item) => (compressedArray[item] = (compressedArray[item] || 0) + 1)
    ); // Recursive step

    return compressedArray;
}

const decompressedList = [...prompt('Enter what you desire')].sort();
// Transformed the message typed by the user into an array and arranged each character alphabetically

console.log(compressedList(decompressedList));
