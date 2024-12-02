#3) შექმენით 3 სხვადასხვა Drop-Down Menu, 3 სხვადასხვა თემაზე თქვენი ფანტაზიით
def dropdown_menu(title, options):
    print(f"\n{title}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("აირჩიეთ ნომერი: "))
    return options[choice - 1]

# თემა 1: ფერები
colors = ["წითელი", "ლურჯი", "მწვანე", "ყვითელი", "თეთრი"]
selected_color = dropdown_menu("აირჩიეთ ფერი:", colors)
print(f"თქვენ აირჩიეთ ფერი: {selected_color}")

# თემა 2: ქალაქები
cities = ["თბილისი", "ბერლინი", "მილანი", "ნიუ-იორკი", "ტოკიო"]
selected_city = dropdown_menu("აირჩიეთ ქალაქი:", cities)
print(f"თქვენ აირჩიეთ ქალაქი: {selected_city}")

# თემა 3: სპორტი
sports = ["ფეხბურთი", "კალათბურთი", "ჩოგბურთი", "თხილამურებით სრიალი", "გოლფი"]
selected_sport = dropdown_menu("აირჩიეთ სპორტი:", sports)
print(f"თქვენ აირჩიეთ სპორტი: {selected_sport}")
