#შეამოწმე, არის თუ არა მომხმარებლის რიცხვი დადებითი.

number = int(input("შეიყვანე რიცხვი: "))

# დადებითობის შემოწმება
if number > 0:
    print("შემოტანილი რიცხვი დადებითია.")
elif number < 0:
    print("შემოტანილი რიცხვი უარყოფითია.")
else:
    print("შემოტანილი რიცხვი ნულია.")
