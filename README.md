# secureworks
Test Case 1 test.txt

This is the initial file with the given input.

Result:
abcde
edcba

Test Case 2 test2.txt

This is blank. This should cause an error to be thrown.

Result:
  File "longestword.py", line 16, in <module>
    print(longestword('test2.txt'))
  File "longestword.py", line 7, in longestword
    max_len = len(max(words, key=len))
ValueError: max() arg is an empty sequence

Test Case 3 test3.txt

This has a little bit longer word with a colon in it.

Result:
sdakjgfjkldsahg;lahgla
alghal;ghasdlkjfgjkads

Test Case 4 test4.txt

This has number and letters and punctuation altogether.

Result:
;;;'''...,,,00998387737372737277283891
19838277273727373778389900,,,...''';;;
