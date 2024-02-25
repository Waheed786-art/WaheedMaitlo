# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import random
import string
a = str(input("Enter the word which contains atleast 3 characters: "))
b = input('Enter "e" to encode and "d" to decode: ')
c = a.clear(" ")
if (b == "e"):
    rand_start = ''.join(random.choices(string.ascii_lowercase, k=3))
    rand_end = ''.join(random.choices(string.ascii_lowercase, k=3))
    new = a[1:] + a[0]
    nword = rand_start+new+rand_end
    print(nword)
    
