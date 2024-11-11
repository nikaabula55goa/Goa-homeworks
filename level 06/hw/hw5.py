#    5) მომხარებელს შემოატანინე input შეამოწმე, არის თუ არა რიცხვი 10-ზე მეტი ან ტოლი.
num1 = int(input("enter number"))

#შევამოწმოთ მეტია თუ არა

if num1 > 10:
    print("more then 10")
elif num1 == 10:
    print("is equal to 10")
else:
    print("less 10")

