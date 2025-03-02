let number = parseInt(prompt("შემოიტანეთ რიცხვი:"));
let choice = prompt("აირჩიეთ: 'ლუწი', 'კენტი', 'კვადრატი', '3-ის ჯერადი'");

for (let i = 1; i <= number; i++) {
    if (choice === 'ლუწი' && i % 2 === 0) {
        console.log(i); // ლუწი რიცხვი
    } else if (choice === 'კენტი' && i % 2 !== 0) {
        console.log(i); // კენტი რიცხვი
    } else if (choice === 'კვადრატი' && Math.sqrt(i) % 1 === 0) {
        console.log(i); // კვადრატი რიცხვი
    } else if (choice === '3-ის ჯერადი' && i % 3 === 0) {
        console.log(i); // 3-ის ჯერადი რიცხვი
    }
}
