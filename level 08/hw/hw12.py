#შეამოწმე, არის თუ არა მომხმარებლის შემოტანილი ორი რიცხვი ერთმანეთზე მეტი და 10-ის ჯერადი.
number1 = int(input("შეიყვანე პირველი რიცხვი: "))
number2 = int(input("შეიყვანე მეორე რიცხვი: "))

# შემოწმება, არის თუ არა რიცხვები ერთმანეთზე მეტი და 10-ის ჯერადი
if number1 > number2 and number1 % 10 == 0 and number2 % 10 == 0:
    print("ორივე რიცხვი არის 10-ის ჯერადი და პირველი რიცხვი მეტია მეორე რიცხვზე.")
else:
    print("ორივე პირობა არ არის შესრულებული.")
