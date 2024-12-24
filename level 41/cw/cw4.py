# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"
def get_middle(s):
    length = len(s)
    if length % 2 == 0:
        return s[length // 2 - 1:length // 2 + 1]
    else:
        return s[length // 2]
