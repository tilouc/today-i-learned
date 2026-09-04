# for loops
# for item in collection:
    # print(item)

for item in 'louis camara':
    print(item)

for item in [1,2,3,4,5]:
    print(item)

for item in {1,2,3,4,5}:
    print(item)

for item in (1,2,3,4,5):
    print(item)
    print(item)
    print(item)
print(item)
# print('hi')

for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(item, x)

#iterable - list, dictionary, tuple, set, string
#iterated -> one by one check each item in the collection.

user = {
    "name": "Golem",
    "age": 5006,
    "can_swim": False
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for item in user.items():
    key, value = item;
    print(key, value)

for key, value in user.items():
    print(key, value)

# for item in 50:
    # print(item) # invalid because int object is not iterable

# exercise counter
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

for item in my_list:
    counter += item

print(counter)

# range
print(range(0,100))

for number in range(0,100):
    print(number)
    print('email list')

for _ in range(0,10):
    print(_)

for _ in range(0,10,2):
    print(_)

for _ in range(10, 0,-1):
    print(_)

for _ in range(10, 0, -2):
    print(_)

for _ in range(10, 0, -2):
    print(list(range(10)))

for _ in range(2):
    print(list(range(10)))

#enumerate
for i, char in enumerate('Hello'):
    print(i, char)

for i, char in enumerate([1,2,3]):
    print(i, char)

for i, char in enumerate((1,2,3)):
    print(i, char)

for i, char in enumerate(list(range(100))):
    print(i, char)

for i, char in enumerate(list(range(100))):
    # print(i, char)
    if char == 50:
        print(f'index of {char} is: {i}')

#while loops

# while condition:
    # do_something

i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('done with all the work')

my_list = [1,2,3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break

#break, continue, pass
my_list = [1,2,3]
for item in my_list:
    # print(item)
    # break
    # continue
    pass
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    # break
    # continue
    pass
    # print(my_list[i])

#Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if (pixel):
            print(fill, end='')
        else:
            print(empty, end='')
    print('') # need a new line after every row

# what is good code?
# clean
# readability
# predictability
# DRY

# Exercise: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)