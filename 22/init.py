#!/usr/bin/env python

# sed 's/,/\n/g' names.txt | sed 's/"//g' > sorted.txt

def sumLetter(alphalist, name):
    result = 0
    for letter in name:
        result += alphalist.index(letter)+1
    return result


alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphalist = alphabet.split()

totalsum = 0
for i, name in enumerate(open('sorted.txt', 'r')):
    totalsum += sumLetter(alphalist, name.strip()) * (i+1)
print totalsum
