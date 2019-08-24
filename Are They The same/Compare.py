def comp(array1, array2):
    if array1 is not None and array2 is not None:
        if len(array1) == len(array2):
            computed = [i**2 for i in array1]
            computed.sort()
            array2.sort()
            return(True if computed == array2 else False)
