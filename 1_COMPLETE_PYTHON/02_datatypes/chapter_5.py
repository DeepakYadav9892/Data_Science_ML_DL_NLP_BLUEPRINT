"""In Python, a string is an immutable sequence of Unicode characters. Indexing allows access to individual characters, while slicing extracts substrings using start, end, and step values. 
Encoding converts strings into bytes so that computers can store and transmit text data, and decoding converts bytes back into readable strings."""

s1 = "Hello"
s2 = 'World'
s3 = """This is
a multiline string"""
# Positive Indexing
word = "Python"

print(word[0])   # P
print(word[3])   # h
#Negative Indexing 
print(word[-1])  # n
print(word[-3])  # h


"""STRING SLICING
What is Slicing?
Slicing means extracting a part of a string.
string[start:end:step]"""

text = "Programming"
print(text[0:6])   # Progra
print(text[3:8])   # gramm

text = "Python"
print(text[0:6:2])   # Pto
text = "Python"
print(text[::-2])   # nohtyP


"""

-6  -5  -4  -3  -2  -1
 P   y   t   h   o   n


String:  P  r  o  g  r  a  m  m  i  n  g
Index:      0  1  2  3  4  5  6  7  8  9  10

Index:  -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
Char:    P   r   o   g   r   a   m   m   i   n   g

"""