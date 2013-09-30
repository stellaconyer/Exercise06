from sys import argv
import re

# get file
filename = argv[1]

# open file
# strip out the new line characters and split on whitespace
input_file = open(filename)
text = input_file.read()
text = re.sub(r'\W+', ' ', text)
text = text.split()

# create empty dictionary
wordcount_dict = {}

# for each word in the input_file
for word in text:
    # if the word is in the wordcount_dict
    if word in wordcount_dict:
        #add to the word count
        wordcount_dict[word] += 1
    # else create a key in the dictionary and set the value to 1
    else:
        wordcount_dict.setdefault(word, 1)
#iterate through the dictionary to print keys and values
for key, value in wordcount_dict.iteritems():
    print key,
    print value

# close file
input_file.close()