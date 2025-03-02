let randomNumbers = [];
let sum = 0;


for (let i = 0; i < 10; i++) {
    randomNumbers.push(Math.floor(Math.random() * 100) + 1); // რიცხვი 1-დან 100-მდე
}


for (let i = 0; i < randomNumbers.length; i++) {
    sum += randomNumbers[i];
}

console.log("რენდომ რიცხვები:", randomNumbers);
console.log("რიცხვების ჯამი:", sum);
