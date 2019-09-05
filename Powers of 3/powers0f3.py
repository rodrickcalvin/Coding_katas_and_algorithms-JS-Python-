import math
def largestPower(N):
    print(math.ceil(math.log10(N)/math.log10(3))-1)

largestPower(81)
