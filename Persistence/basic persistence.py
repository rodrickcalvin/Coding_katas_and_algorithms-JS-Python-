from functools import reduce


def persistence(num):
    if (num > 9):
        times = []
        while num > 9:
            times.append(num)
            arr = [int(i) for i in str(num)]
            mult = reduce(lambda x, y: x*y, arr)

            if mult > len(arr):
                num = mult
                arr = [int(i) for i in str(num)]
            else:
                break
        return (len(times))
    else:
        return (0)
