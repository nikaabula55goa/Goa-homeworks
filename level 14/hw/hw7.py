#)Print numbers divisible by both 3 and 5 from 1 to 100 inclusive.
# for loop-ის გამოყენება რიცხვების გამოსატანად, რომლებიც იყოფა 3-ზე და 5-ზე 1-დან 100-მდე
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:  # თუ რიცხვი იყოფა 3-ზე და 5-ზე
        print(i)
