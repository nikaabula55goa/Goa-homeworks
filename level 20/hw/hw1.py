#1) შექმენით სია რომელშიც იქნება 15 ელემენტი შემდეგ გამოიტანეთ სიის ყველა ელემენტი while loop-ის გამოყენებით და ასევე for loop-ითაც
# 15 ელემენტიანი სიის შექმნა
sia = ["ელემენტი1", "ელემენტი2", "ელემენტი3", "ელემენტი4", "ელემენტი5", 
       "ელემენტი6", "ელემენტი7", "ელემენტი8", "ელემენტი9", "ელემენტი10", 
       "ელემენტი11", "ელემენტი12", "ელემენტი13", "ელემენტი14", "ელემენტი15"]

print("სიის ელემენტები while ციკლით:")
# while ციკლის გამოყენებით
index = 0
while index < len(sia):
    print(sia[index])
    index += 1

print("\nსიის ელემენტები for ციკლით:")
# for ციკლის გამოყენებით
for element in sia:
    print(element)
