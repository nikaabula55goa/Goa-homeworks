#4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი
def check_sign(number):
    if number > 0:
        return "დადებითი"
    elif number < 0:
        return "უარყოფითი"
    else:
        return "ნული"

# ფუნქციის გამოძახება
num = float(input("შეიყვანეთ რიცხვი: "))
print(check_sign(num))
