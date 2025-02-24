#user defined variables


#loading a module
#keywords - have meaning in that language
#identifiers- words that are defined by user
import keyword

print(keyword.kwlist)
"""

['False', 'None', 'True', 'and', 'as', 
'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for', 'from',
   'global', 'if', 'import', 'in', 'is', 
   'lambda', 'nonlocal', 'not', 'or', 
   'pass', 'raise', 'return', 'try', 
   'while', 'with', 'yield']
"""

print(True)
# print(true) Nameerror: name 'true' is not defined

my_value='something'
print(my_value)

#True= something
#syntax error: cannot assign to True

print(keyword.iskeyword('True')) #True
print(keyword.iskeyword('true')) #False
print(keyword.iskeyword('my_value')) #False

"""
Identifiers - user defined variables
Naming convention

1. first characters:A-Z,a-z, _
2. keywords should not be used as identifiers
3. remaining chars: a-z, A-Z, 0-9, _

Rule 1:
True=123 # syntax error

PEP 8 - Dont create names similar to keywords
e.g: ture = 123

Rule 2:

PEP8 recommends to use capitals for constants
PI=3.1416
DOZEN=12


OOP-> name mangling
Variable -> public variable
_variable -> protected variable
__variable -> Private variable

__variable__ -> Built in function
Ex: __file__, __name__, __doc__

"""