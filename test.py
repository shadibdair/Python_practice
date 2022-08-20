
# For testing 

with open("Alice.txt",'r') as data_file:
    for line in data_file:
        data = line.split()
        #print(data)
    frequent_word = ""
    frequency = 0
            
    # Finding the max occurred word
    for i in range(0, len(data)):
        
        # Declaring count
        count = 1;
        
        # Count each word in the file
        for j in range(i+1, len(data)):
            if(data[i] == data[j]):
                count = count + 1;

        # If the count value is more
        # than highest frequency then
        if(count > frequency):
            frequency = count;
            frequent_word = data[i];

    print("Most repeated word: " + str(frequent_word))
    print("Frequency: " + str(frequency))