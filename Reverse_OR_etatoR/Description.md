# Reverse OR etatoR(rotate)

This is a function that takes in:
* A string - The ```str``` must be one of digits.```[strng]```
* An integer - The ```int``` is a size of chunks.```[sz]```

>EXAMPLE:

**If:**
```
strng ='123456987654' sz = 6
```
**It returns:**
```
234561876549
```
**A chunk** is a string```[str]``` divided into strings of length ```[sz]```.

## Conditions to meet:
* ```strng``` must not be empty or ```sz``` must not be ```<= 0```.
* ```sz``` must not be ```>``` the ```len(strng)```

* If condition is either of the two ```return ""```

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.