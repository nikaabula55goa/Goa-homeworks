#დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა მომხმარებლის შემოტანილი რიცხვი 100-ზე მეტი და ლუწი.

number = int(input("შეიყვანე რიცხვი: "))

# შემოწმება, არის თუ არა რიცხვი 100-ზე მეტი და ლუწი
if number > 100 and number % 2 == 0:
    print("შემოტანილი რიცხვი 100-ზე მეტია და ლუწია.")
else:
    print("შემოტანილი რიცხვი ან არ არის 100-ზე მეტი, ან არ არის ლუწი.")
