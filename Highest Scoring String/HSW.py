def high(x):
    str = x.split(' ')
    pos, totalscore = [],[]
    for i in str:
        for j in i:
            pos.append(ord(j)-96)
        totalscore.append(sum(pos))
        pos.clear()
    print(str[totalscore.index(max(totalscore))])
        
high('what time are we climbing up the volcano')