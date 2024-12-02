def sum_str(a, b):
    # If a or b is an empty string, treat it as "0"
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)