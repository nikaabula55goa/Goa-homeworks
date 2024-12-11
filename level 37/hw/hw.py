#      2) გააკეთეთ random student generator რომელსაც გადაეცემა ჯგუფის მოსწავლეებით სავსე სია და დაგვიბრუნებს რენდომულად განაწილებულ გუნდებს მზგავსად როგორც გავაკეთეთ წინა გაკვეთილზე 
import random

def generate_random_groups(students, group_size):
    # სია რანდომულად შერყეული
    random.shuffle(students)
    
    # ჯგუფების ჩამოყალიბება
    groups = []
    for i in range(0, len(students), group_size):
        groups.append(students[i:i+group_size])
    
    return groups

# მაგალითი
students = ['ნიკა', 'ალეკო', 'მარი', 'სოფო', 'ლუკა', 'გაბრიელი', 'საბა', 'ალეკო', 'ნიკა', 'დათო']
group_size = 3

groups = generate_random_groups(students, group_size)
print(groups)
