# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = 'abracadabra'
# a. Retrieve the 5th character.
fifth_char = magic[4]
# b. Retrieve the second to last character.
stlc = magic[-2]
print(stlc)
# c. Find the first occurrence of the letter 'c'.
fci = print(magic.index('r'))
#d. find lats occurance of letter A
lai = print(magic.rindex('a'))


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
hij = print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
m_index = print(alphabet.index('m'))
es = print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
ra = print(alphabet[: :-1])
ihavedream = "Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity."
rihavedream = print(ihavedream[: :-1])


# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
johnQ = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
john = print(johnQ.find("John F. Kennedy"))
en = print(johnQ[83:])


# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
PythonQ = "Python is fun. Fun is good. Good is subjective."
GoodIsS = PythonQ.find("subjective.")
GoodIsS2 = print(PythonQ[GoodIsS:])
# b. Extract every third word.
third_letter = print(PythonQ[: :3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
words = PythonQ.split()
reversed_words = ' '.join(reversed(words))
print(reversed_words)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
starwarsQ = "MAY THE FORCE BE WITH YOU."
print(starwarsQ.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
motto = ["Make", "haste", "slowly."]
mottoJoined = ' '.join(motto)
print(mottoJoined)
# b. Now, split the string at every occurrence of the letter 'a'.
mottoSplit = mottoJoined.split('a')
print(mottoSplit)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
sentence = "Life is what happens when you are busy making other plans."
replaceBusy = sentence.replace("busy", "distracted")
print(replaceBusy)
# b. Replace "plans" with "mistakes".
replacePlans = sentence.replace("plans", "mistakes")
print(replacePlans)
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.