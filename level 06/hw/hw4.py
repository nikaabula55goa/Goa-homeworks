#4)შემოიტანე 2 input შეამოწმე, არის თუ არა ორი რიცხვის ჯამი 100-ზე მეტი.
num1 = int(input("enter number"))
num2 = int(input("enter number"))

#შევამოწმოთ მათი ჯამი არის თარა 100
if num1 + num2 > 100:
    print("more then 100")
elif num1 +num2 < 100:
    print("less 100")
