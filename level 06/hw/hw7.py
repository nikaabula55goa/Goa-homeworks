#    7) მომხმარებელს შემოატანინეთ სახელი და შეამოწმეთ ეს სახელი უდრის თუ არა თქვენს სახელს
name = input("enter your name")
me = "nika"

#ვნახოთ შემოტანილი სახელი მეტია თუ არა ჩემ სახელზე
if name < me:
    print(">")
elif name == me:
    print("==")
else:
    print("<")