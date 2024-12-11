def digitize(n):
    return [n%10] + digitize(n/10) if n else []