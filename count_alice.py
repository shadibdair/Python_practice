# Open for text file for reading text
#f = open('Alice.txt','r')

# with open('Alice.txt') as f:
#     contents = f.read()
#     print(conte# Python program to find the most repeated word
# in a text file
 # Python program to find the most repeated word
# in a text file

# A file named "gfg", will be opened with the
# reading mode.
file = open("Alice.txt","r")
frequent_word = ""
frequency = 0
words = []

# Traversing file line by line
for line in file:
	
	# splits each line into
	# words and removing spaces
	# and punctuations from the input
	line_word = line.lower().replace(',','').replace('.','').split(" ");
	
	# Adding them to list words
	for w in line_word:
		words.append(w);
		
# Finding the max occurred word
for i in range(0, len(words)):
	
	# Declaring count
	count = 1;
	
	# Count each word in the file
	for j in range(i+1, len(words)):
		if(words[i] == words[j]):
			count = count + 1;

	# If the count value is more
	# than highest frequency then
	if(count > frequency):
		frequency = count;
		frequent_word = words[i];

print("Most repeated word: " + str(frequent_word))
print("Frequency: " + str(frequency))




