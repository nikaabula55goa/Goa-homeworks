#2) მომხმარებელს შეეკითხეთ სახელი შემდეგ დაბეჭდეთ ამ სახელის მესამე ასო
name = input("enter your name")
# შეამოწმოთ, არის თუ არა სახელში 3 ან მეტი ასო
if len(name) >= 3:
    # მესამე ასოს დაბეჭდვა
    print("თქვენი სახელის მესამე ასოა:", name[2])
else:
    print("სახელში საკმარისი ასოები არ არის მესამე ასოს გამოსატანად.")