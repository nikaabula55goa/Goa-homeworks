#3 ) გააკეთეთ სია სადაც იქნება 10 ინტეჯერი , ინტეჯერები რომელიბ იქნება 10 ზე ნაკლები append ის დახმარებით შეიყვანეთ ახალ ცხრილში
full_list = [3, 15, 7, 20, 1, 12, 9, 4, 18, 6]
new_list = []
for რიცხვი in full_list:
    if რიცხვი < 10:
        new_list.append(რიცხვი)

print("ახალი სია:", new_list)