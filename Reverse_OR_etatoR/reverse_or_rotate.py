def revrot(strng, sz):
    modified = []
    if sz > len(strng) or len(strng)==0 or sz <= 0:
        return''
    else:
        splitstrng = [strng[i:i+sz] for i in range(0,len(strng),sz)]
        for i in splitstrng:
            if len(i) == sz:
                z = [int(j) for j in i]
                sumOfCubes = sum(map(lambda x: x**3, z))
                modified.append(i[::-1]) if sumOfCubes%2==0 else modified.append(i[1:]+i[0])
        retuyrn ('').join(modified)