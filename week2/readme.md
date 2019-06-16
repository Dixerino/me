TODO: Reflect on what you learned this week and what is still unclear.

#Revision
LIST
[] - square bracket

TUPPLES
() - round bracket

DICTIONARY
{} - curly brackets
KEY : VALUE pair
    e.g. {'Name':'Cake', 'Taste':'Tasty'}

ITERATIONS
map(function, list) - prints the function for every element in list
for function in list
range

"""doc string"""

TO SUBMIT
1. add
2. push
##Exercise Notes
REMEMBER to return the answer using the command 'return'
#Exercise3
Reset the step list back to an empty one before rerunning the 'for' loop

#COMMANDS
string.upper() makes uppercase
str() makes a string
def function_name(): defines a new function
len() finds the length of a list
a_number % 2 != 0 when a number is divided by 2 is the remainder NOT 0?

#Adding to List
list.append - adds to back of list

#Adding to List using 'for' loops
list = []
for i in range(n):
    list.append(x)
OR
list = [x for x in range(n)]

#Double 'for' loop in one line
coord = [(x,y) for x in range(i) for y in range(s)]
OR 
#'for' loop within a 'for' loop
coord = []
    for x in range(10):
        for y in range(5): 
            coord.append(('(i' + str(x) + ', j' + str(y) + ')'))

#List Splitting
chunks = [coord[i:i+5] for i in range(0, len(coord), 5)] - separates list into mini-lists with 5 elements in each

#DEBUGGING
breakpoint: runs the code until that point
step over: continues the code to the next line
