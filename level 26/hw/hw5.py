#5) შექმენით სია რომელშიც იქნება მოთავსებული რენდომ რიცხვები შემდეგ კი ამ სიიდან ამოშალეთ ყველა ლუწი რიცხვი
import random
random_numbers = [random.randint(1, 100) for _ in range(20)]  # 20 რიცხვი 1-100 დიაპაზონში

odd_numbers = [num for num in random_numbers if num % 2 != 0]

print("რენდომ რიცხვები:", random_numbers)
print("მხოლოდ კენტი რიცხვები:", odd_numbers)
