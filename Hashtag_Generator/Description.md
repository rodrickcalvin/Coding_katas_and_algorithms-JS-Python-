# Hashtag Generator
This is a function that takes in a string(sentence) and returns:
* a string that must start with a hashtag (#).
* A string with all words or letters having their first letter capitalized.
* If the final result is longer than 140 chars it must return false.
* If the input or the result is an empty string it must return false.

>EXAMPLES:
```
Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
```
```
"   Hello     World   "           =>  "#HelloWorld"
```
```
""                                        =>  false
```