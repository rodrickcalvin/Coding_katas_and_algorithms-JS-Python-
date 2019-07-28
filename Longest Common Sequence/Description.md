 # LONGEST COMMON SEQUENCE
 A function that accepts two sequences and returns the longest subsequence common to the passed in sequences.
 ### Subsequence
 > A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.

 #### Examples of subsequences:
 >Subsequences of
 ```"abc"``` = ```"a", "b", "c", "ab", "ac", "bc"``` and ```"abc"```.

#### Examples of imputs and outputs
 ```
lcs( "abcdef" , "abc" ) => returns "abc"
lcs( "abcdef" , "acf" ) => returns "acf"
lcs( "132535365" , "123456789" ) => returns "12356"
 ```

#### Notes
* Both arguments will be strings
* Return value must be a string
* Return an empty string if there exists no common subsequence
* Both arguments will have one or more characters
* All tests will only have a single longest common subsequence. Don't worry about cases such as LCS( ```"1234"```, ```"3412"``` ), which would have two possible longest common subsequences: ```"12" and "34"```.