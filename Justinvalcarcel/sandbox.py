#Code for disabling sys modules that will be inserted into the beginning of the data the user inputs
insert = """
import sys

for x in sys.modules:
    sys.modules[x] = None

"""

#Keywords that are not allowed
badList = [
    '__builtins__', 'open', 'eval', 'execfile', 'import', 'exec','write', 'read',
]

#place the file in the folder of this code and then type in it's name at the prompt
def input():

    file = raw_input("what is your file name? you can type 'testpy.py' "
                     "for fibonacci numbers or 'testpy2.py' for the powers of 2\n")
    test = open(file, 'r')
    return test.read()

code = input()

# looks through the blacklisted word list and if the input file contains it then it's it asks for a different file
for x in badList:
    if x in code:
        print 'not allowed, resetting'
        code = input()

#inserts the disabling of the sys module into the inputted code
code = insert + code

#executes the code
exec(code)

