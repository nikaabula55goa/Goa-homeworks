def square_digits(num):
    number = str(num)
    final_world = ""
    for element in number:
        final_world += str(int(element)* int(element))
    return int(final_world)
#  დავალება codewars იდან