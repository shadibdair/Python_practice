# Open for text file for reading text
#f = open('Alice.txt','r')

with open('Alice.txt') as f:
    contents = f.read()
    print(contents)