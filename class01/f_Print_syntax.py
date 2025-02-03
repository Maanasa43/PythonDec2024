""""

Print function syntax and its usage
escape sequences

 - characters whose presence is felt but they were not printed
 \t - Tab space
 \n - New line
 \b - overwrites previous character

 r'' - raw string



"""

print("hello world Python")

print("hello world \tpython")

# To ignore the escape sequences
print("hello world \\npython")
print (r"Hello \tWorld \npython")

# print ()
# print(data, sep='', end='\n')

print('hello world')
print('hello') # default end=\n
print('world')

print('hello', end='\t')
print('world') # default end=\n

print('hello', end='____')
print('world') # default end=\n

#print('hellow\r world') # \r - overwrites complete existing line

# ASCII characters
# unicode characters
