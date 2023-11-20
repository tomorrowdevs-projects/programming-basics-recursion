function getFlat(array) {

    if (!array.length) return array;

    if (Array.isArray(array[0])) {
        const list1 = getFlat(array[0]);
        const list2 = getFlat(array.slice(1));
        return [...list1, ...list2];
    }
    else {
        const list1 = [array[0]];
        const list2 = getFlat(array.slice(1));
        return [...list1, ...list2];
    }
}

const array = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]];

console.log(getFlat(array));