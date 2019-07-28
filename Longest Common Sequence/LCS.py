def lcs(x, y):
    result = ''
    for i in y:
        if i in x:
            result += i
            x = x[x.index(i) + 1::]
    return result