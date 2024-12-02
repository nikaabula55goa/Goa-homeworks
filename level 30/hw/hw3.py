#3) შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი
def check_parity(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

# ფუნქციის გამოძახება
num = int(input("შეიყვანეთ რიცხვი: "))
print(check_parity(num))
