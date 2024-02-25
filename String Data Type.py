name = "Waheed"
friend = "Hussain"
anotherFriend = "Atif"
apple = 'He said, "I want to eat an apple"'
# triple quotation is used to make string of multiple line easily and conveniently.
mango = '''She said, 
"I want to eat an apple"
'''

print("Hello!",name)
print(mango)
print(apple)
print(name[0])  # it will print first letter of name..
print(name[1])  # it will print second letter of name..
print(name[2])  # it will print third letter of name..

print("Let's use a for loop\n")

for character in name:    # change the name if we want to make loop of any other...  It is a loop for string..
    print(character)
    
    
f = '''Direct Sentence:    He said to me,"Do you study at home?"'''
g = '''Indirect Sentence:  He said whether I studied at home'''
print(f)
print(g)