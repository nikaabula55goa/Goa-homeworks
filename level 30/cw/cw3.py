#3) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია ხოლო ფუნქცია დააბრუნებს ამ სიის ელემენტების ჯამს
def sum_of_list(numbers):
    """
    იღებს რიცხვებით სავსე სიას და აბრუნებს მისი ელემენტების ჯამს.
    :param numbers: რიცხვებით სავსე სია
    :return: სიის ელემენტების ჯამი
    """
    return sum(numbers)

# ფუნქციის გამოყენება
numbers_list = [3, 7, 12, 5, 10]  # რიცხვებით სავსე სია
result = sum_of_list(numbers_list)

print("სია:", numbers_list)
print("სიის ელემენტების ჯამი:", result)
