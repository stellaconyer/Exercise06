from sys import argv
import re

def normalize(text):
    text = re.sub(r'\W+', ' ', text)
    text = text.lower().replace("_", "")

    return text

# get file
filename = argv[1]

# open file
# strip out the new line characters and split on whitespace
input_file = open(filename)
text = input_file.read()

text = normalize(text)
text = text.split()

# create empty dictionary
wordcount_dict = {}

# for each word in the input_file
for word in text:
    # if the word is in the wordcount_dict
    # if word in wordcount_dict:
    #     #add to the word count
    #     wordcount_dict[word] += 1
    # # else create a key in the dictionary and set the value to 1
    # # else:
    # wordcount_dict.get(word, 0)
    # wordcount_dict[word] += 1
    wordcount_dict[word] = wordcount_dict.get(word, 0) + 1

#iterate through the dictionary to print keys and values
# for key, value in wordcount_dict.iteritems():
#     print key,
#     print value

count = {}
for key, value in wordcount_dict.iteritems():
    count[value] = wordcount_dict.get(value, [])
    count[value].append(key)
print count   


# list_of_words=[]
# for key, value in wordcount_dict.iteritems():
#     list_of_words.append((value, key))
#     sorted(list_of_words)
# print list_of_words

# close file
input_file.close()

#, key = lambda a: -a[0]