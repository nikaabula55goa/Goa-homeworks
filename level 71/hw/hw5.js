let numbers = [3, -5, 7, -2, -8, 4];

numbers.forEach((num, i, arr) => {
    if (num < 0) arr.splice(i, 1, 0);
});

console.log(numbers);
