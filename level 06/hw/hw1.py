#  1) შექმენი ორი input შეადარე ორი რიცხვი და დაბეჭდე შედეგი.
# ორი რიცხვის შეყვანა
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

# შედარება და შედეგის დაბეჭდვა
if num1 > num2:
    print("პირველი რიცხვი მეტია მეორეზე.")
elif num1 < num2:
    print("მეორე რიცხვი მეტია პირველს.")
else:
    print("ორივე რიცხვი თანაბარია.")