#დავალება: მომხამრებლს შემოატანინეთ 2 რიცხვი, ხოლო შემდეგ გაკეთეთ ამ რიცხვებს შორის მათემატიკური ოპერაცია, და შეინახეთ ცვლადში, ხოლო ბოლოს დაპრინტეთ ცვლადის მნიშვნელობა.
num1 = int(input("შეიტანეთ პირველი რიცხვი: "))
num2 = int(input("შეიტანეთ მეორე რიცხვი: "))

# ოპერაციის არჩევა
operation = input("აირჩიეთ ოპერაცია (+, -, *, /): ")

# ოპერაციის შესრულება და შედეგის შენახვა
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "გაყოფა ნულზე არ შეიძლება"
else:
    result = "არასწორი ოპერაცია"

# შედეგის გამოყვანა
print(f"შედეგი: {result}")
