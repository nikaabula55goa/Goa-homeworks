#2)  შექმენით პროგრამა რომელიც დაითვლის სიაში რამდენჯერ მეორდება თქვენი სახელი არ გამოიყენოთ count ფუნქცია 
names = ["ნიკა", "კატო", "ნიკა", "თენგიზი", "ნიკა", "მარიამი", "კატო", "ლევანი", "კატო", "ანა", "კატო"]

my_name = "ნიკა"

my_name_count = 0

for name in names:
    if name == my_name:
        my_name_count += 1

print("სახელი", my_name, "სიაში გვხვდება", my_name_count, "ჯერ")
