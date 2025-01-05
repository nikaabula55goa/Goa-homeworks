def epley(w, r):
    return w * (1 + r/30)


def mcglothin(w, r):
    return (100*w) / (101.3 - 2.67123*r)


def lombardi(w, r):
    return w*r**0.10


def calculate_1RM(w, r):
    if r == 0: return 0
    if r == 1: return w
    return round(max(epley(w, r), mcglothin(w, r), lombardi(w, r)))