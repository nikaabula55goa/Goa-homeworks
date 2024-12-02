#2) შექმენით რამდენიმე ფუნქცია სხვადასხვა მათემატიკური მოქმედებებისთვის ერთში, დაუმატეთ რიცხვები მეორეში გაამრავლეთ ....
# დამატების ფუნქცია
def add_numbers(a, b):
    """
    ამატებს ორ რიცხვს.
    :param a: პირველი რიცხვი
    :param b: მეორე რიცხვი
    :return: ორი რიცხვის ჯამი
    """
    return a + b

# გამოკლების ფუნქცია
def subtract_numbers(a, b):
    """
    გამოაკლებს b-ს a-ს.
    :param a: პირველი რიცხვი
    :param b: მეორე რიცხვი
    :return: გამოკლების შედეგი
    """
    return a - b

# გამრავლების ფუნქცია
def multiply_numbers(a, b):
    """
    ამრავლებს ორ რიცხვს.
    :param a: პირველი რიცხვი
    :param b: მეორე რიცხვი
    :return: ორი რიცხვის ნამრავლი
    """
    return a * b

# გაყოფის ფუნქცია
def divide_numbers(a, b):
    """
    ჰყოფს a-ს b-ზე. თუ b არის 0, დაბრუნდება შეცდომის შეტყობინება.
    :param a: პირველი რიცხვი
    :param b: მეორე რიცხვი
    :return: გაყოფის შედეგი ან შეცდომის შეტყობინება
    """
    if b == 0:
        return "შეუძლებელია გაყოფა 0-ზე!"
    return a / b

# ფუნქციების გამოძახება
num1 = 10
num2 = 5

print("რიცხვები:", num1, "და", num2)
print("დამატება:", add_numbers(num1, num2))
print("გამოკლება:", subtract_numbers(num1, num2))
print("გამრავლება:", multiply_numbers(num1, num2))
print("გაყოფა:", divide_numbers(num1, num2))
