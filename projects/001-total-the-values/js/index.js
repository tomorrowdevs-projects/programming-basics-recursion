'use strict';

function getSum() {
    let num = parseFloat(
        prompt(
            'Enter a number or If you want to stop the programme, press Enter as a black line.'
        )
    );
    // If the value entered is an empty string or num is not a number
    if (num === '' || isNaN(num)) {
        return 0.0;
    } else {
        // num + recursive function getSum()
        return num + getSum();
    }
}
console.log(`The sum of the entered values is ${getSum()}`); // Total
