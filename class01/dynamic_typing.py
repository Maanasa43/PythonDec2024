"""
python is a dynamic typing language
Progrmming language type

1.static language type
first define a variable and then use them

2. dynamic language type
create when you need, no declaration need

python code --> pyhton byte code --> pythonInterpreter --> c compiler
pythonis slower compared to compiler based languages
it will take line by line or block by block based execution




"""

num=123
type(num)
print(type(num))

print ("num=", num)
print ("num=", num, "type=", type(num))

# it is a dynamic language

num=200
print ("num=", num, "type=", type(num))  #int

num=300.0
print ("num=", num, "type=", type(num)) #float

num=300.
print ("num=", num, "type=", type(num)) #float

num=300,
print ("num=", num, "type=", type(num)) #tuple

#tuple is a data structure in python

num=-0.09
print ("num=", num, "type=", type(num)) #float

num=-0.09j
print ("num=", num, "type=", type(num)) #complex value

num="300"
print ("num=", num, "type=", type(num)) #string

num="three"
print ("num=", num, "type=", type(num))  #string

num= True
print ("num=", num, "type=", type(num)) #boolean

"""num= true, case sensitive language
print ("num=", num, "type=", type(num)) #throws error"""

num=False
print ("num=", num, "type=", type(num)) # Boolean

num=None
print ("num=", num, "type=", type(num)) #none

num='None'
print ("num=", num, "type=", type(num))