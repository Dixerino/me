"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#I think this defines a list called some_words
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #it defined a list with the words 'what', 'does', 'this', 'do', and '?'

#I think this will print out the words in the list one at a time
for word in some_words:
    print(word) #it printed out the words in the list one line at a time

#I think this prints out the words in the list one at a time
for x in some_words:
    print(x) #it printed out the words in the list one line at a time

#I think this prints the some_words list
print(some_words)

#I think this prints 'some_words contains more than 3 words' if the list has more than 3 words; in this case, it would print
if len(some_words) > 3:
    print('some_words contains more than 3 words') #it printed 'some_words constains more than 3 words

#I think this identifies the platform running the code
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction() #it printed my laptop's information including system, node, release, version, machine, and processor
