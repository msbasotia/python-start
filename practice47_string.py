message = "This is a lorem ipsum text."

print(message)
print(message[0])
print(message[0],message[1],message[2],message[3],message[4],message[5],message[6])
print(len(message))
print(message[5:12])
print(message[5:])
print(message[:12])


print("Index of first space :", message.index(' '))

first_space_index = message.index(' ')

print("Text after first space :",message[first_space_index+1:])


last_space_index = message.rindex(' ')

print("Text before last space :",message[:last_space_index])

words = message.split(' ')
print(words) # to get all the words of a string you can first convert it to a word list and then use this list to find words

# https://www.w3schools.com/python/python_ref_string.asp
# https://docs.python.org/3/library/stdtypes.html#string-methods