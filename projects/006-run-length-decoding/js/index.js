function decodeRunLength(array) {
    // Base case
    if (!array.length) return array;
    // Recursive path
    let list = [];
    for (let i = 0; i < array[1]; ++i) {
        list += array[0];
    }

    return [...list, ...decodeRunLength(array.slice(2))];
}

const compressedList = ["A", 12, "B", 4, "A", 6, "B", 1, "C", 10];
console.log(`Compressed list: ${compressedList}`);

console.log(`Decompressed list: ${decodeRunLength(compressedList)}`);