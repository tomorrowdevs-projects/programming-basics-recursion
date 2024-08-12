/* Caso base: condizione di uscita dalla ricorsione
e
Passo ricorsivo
Richiamo la mia funzione fintantoche non raggiungo il caso base. Nel mio esercizio la condizione di uscita è una stringa vuota
*/
const prompt = require('prompt-sync')();
// function getSum() {
//     const value = prompt('Enter a value');
//     // Caso base: se l'utente digita enter
//     if (value === '') {
//         return 0;
//     }
//     // Adesso c'è il passo ricorsivo - Adesso prendo il valore e prendo il return
//     return Number(value) + getSum();
//     // Se ricevo una stringa vuota, esco dalla ricorsione
//     // altrimenti prendo
// }
// console.log(getSum());
function getSum() {
    const value = prompt('Enter a value');
    return value === '' ? 0 : Number(value) + getSum();
}
console.log(getSum());
