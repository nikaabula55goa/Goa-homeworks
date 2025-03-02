let number = parseInt(prompt("შემოიტანეთ რიცხვი:"));
let i = 1;

while (i <= number) {
    if (i % 3 === 0 && i % 5 === 0) {  // იმ რიცხვების შემოწმება, რომლებიც 3-ის და 5-ის ჯერადები არიან
        console.log(i);
    }
    i++;
}
