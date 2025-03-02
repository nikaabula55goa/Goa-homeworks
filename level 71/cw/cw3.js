let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; // რიცხვებით სავსე სია
let sumOfSquares = 0;

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {  // ლუწი რიცხვის შემოწმება
        sumOfSquares += numbers[i] ** 2;  // ლუწი რიცხვის კვადრატი
    }
}

console.log("ლუწი რიცხვების კვადრატების ჯამი:", sumOfSquares);
