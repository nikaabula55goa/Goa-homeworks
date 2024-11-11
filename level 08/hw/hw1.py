#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი  რიცხვი 10-ზე ნაკლები.
num1 = int(input("enter number"))

#შევამოწმოთ მეტია თუ არა

if num1 > 10:
    print("more then 10")
elif num1 == 10:
    print("is equal to 10")
else:
    print("less 10")
