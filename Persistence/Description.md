# Persistence
This a function that takes in a number(num) and returns the number of times every digit of num is multiplied and reduced down to the product being a single digit.

## Examples:
### Ex1:
> 1. num = 2345  ->  (2x3x4x5) = 120  ->  (1x2x0) = 0
> persistence(2345) returns 2

This is because it gets a product twice.

###  Ex2:
> 2. num=999 ->(9x9x9)=729 ->(7x2x9)=126 ->(1x2x6)=12 ->2
> persistence(999) returns 4