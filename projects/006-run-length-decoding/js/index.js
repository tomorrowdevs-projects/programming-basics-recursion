function decodeRunLength(array) {
    // Base case
    if (!array.length) return array;
    // Recursive path
    let list = [];
    for (let i = 0; i < array[1]; ++i) {
        list.push(array[0]);
    }

    return [...list, ...decodeRunLength(array.slice(2))];
}

const compressedList = ["A", 2, "B", 4];
console.log(`Compressed list: ${compressedList}`);

console.log(`Decompressed list: ${decodeRunLength(compressedList)}`);