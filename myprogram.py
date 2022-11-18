#pip install termcolo
from termcolor import colored

#define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


#Program to sort alphabetically the words from a string provided by the user
my_str = "Hello, World. How are you?"

#https://pastebin.com/9xcTchz4
#remove punctuation
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

#breakdown the string into a list of words
words = [word.lower() for word in no_punct.split()]

#sort the list
words.sort()

#disiplay the sorted words
print("The sorted words are:")
for word in words:
    print(colored(word, 'blue'))