#3) მომხმარებელს შემოატანინეთ ორი რიცხვი ხოლო ამის შემდეგ for loop - ის გამოყენებით გამოიტანეთ ამ რიცხვებს შორის ჯამი და ნამრავლი.
start = int(input("შეიყვანეთ პირველი რიცხვი: "))
end = int(input("შეიყვანეთ მეორე რიცხვი: "))

total_sum = 0
total_product = 1
for i in range(start, end + 1):
    total_sum += i
    total_product *= i

print(f"{start} და {end} შორის რიცხვების ჯამი: {total_sum}")
print(f"{start} და {end} შორის რიცხვების ნამრავლი: {total_product}")
