

# Lists In Python

x = [4,6,9,10,21]
print(x[2])
print(x[-1])

# Slicing in Python
x = ['a', 'b', 'c', 'd', 'e']
# Negative slicing
# -5     -4     -3     -2     -1
print(x[0 : 3]) # ['a' , 'b', 'c'] will get printed
print(x[-3 : ])
print(x[-5 : -2])

# Posetive slicing
x = [1, 2, 3, 4, 5, 6]
print(x[  : 3])

# Slicing with steps
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[0 : 9 : 2])

# Functions in Python
def BMI(mass, height):
    if height > 100:
        height = height / 100
    else :
        height = height
    return mass/ height ** 2

print(BMI(53, 1.72))

# Dictionaries in Python
country = {
    'Ethiopia' : 'Addis Ababa',
    'Kenya' : 'Nairobi',
    'Turkiye' : 'Ankara',
    'Iran' : 'Theran'
}

print(country['Kenya']) #Will return Nairobi
print('Ethiopia' in country) # Will return True if it exist False if it's not

# Loops in Python
# Try to print 1 up to 100

# i: While Loop

i = 1
while i <= 100:
    print(i)
    i += 1

print(' ')
# ii: For Loop
c = 1
for c in range(101):
    print(c)