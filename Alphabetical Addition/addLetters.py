import string
def add_letters(*letters):
    sum = 0
    if len(letters)==0:
        return'z'
    for x in letters:
        sum = sum+(ord(x)-96)
    if sum>26:
        sum = sum - 26
    print(sum)
    print(string.ascii_lowercase[sum-1])


add_letters('z', 'b', 'c')