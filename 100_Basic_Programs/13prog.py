"""13.Write a program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
"""

x=input('enter:')
d={"DIGITS":0,"LETTERS":0}
for c in x:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass

print('Letters:',d["LETTERS"])
print('Digits:',d["DIGITS"])