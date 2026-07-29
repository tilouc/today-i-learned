# conditions
value = True
if value:
    print("true")
else:
    print("false")
# is_old = True
is_old = bool('hello')
# is_old = False
# is_licenced = True
is_licenced = bool(5)
# is_licenced = False

#truthy and falsy
print(bool('hello'))
print(bool(5))

print(bool(''))
print(bool(0))
print(bool(None))

if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')
# elif is_licenced:
    # print('you can drive now!')
else:
    print('you are not of age!')

print('ok ok ok')

password = '123'
username = 'johnny'

if password and username:
    print('welcome!')

# ternary operator

# condition_if_true if condition else condition_if_false
is_friend = True
# is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

# short circuiting
is_friend = True
is_user = True

print(is_friend and is_user)

if is_friend and is_user:
    print('best friends forever')

is_friend = True
is_user = False

if is_friend or is_user:
    print('best friends forever')

is_friend = False
is_user = True

if is_friend and is_user:
    print('best friends forever')


#logical operators
# >
# <
# ==
print(4 > 5)
print(4 < 5)
print(4 == 5)
print('hello' == 'hello')
print('a' > 'b') # compares unicode numbers
print('a' > 'A')
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 < 4)
print(1 >= 0)
print(1 <= 0)
print(0 <= 0)
print(0 != 0)
print(0 != 1)

print(not(True))
print(not(False))
print(not(1 == 1))

#exercise
# is_magician = False
is_magician = True
is_expert = True

# check if magician AND expert: "you are a master magician"
if is_expert and is_magician:
    print("you are a master magician")

# check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")

# if you're not a magician: "you need magic powers"
elif not is_magician:
    print("you need magic powers")

#is vs ==
print(True == 1) # True (True == bool(1))
print(True == '') # False
print(True == ' ') # False
print('' == 1) # False
print('1' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True
print([1,2,3] == [1,2,3]) # True

print(True is 1) # False
print(True is True)
print('1' is '1') # object caching
print('1' is 1) # False
print([] is 1) # False
print([] is [])
print(10 is 10.0) # False
print(10 is 10)
print(256 is 256)
print(257 is 257)
print([1,2,3] is [1,2,3]) # False
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b)

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
    break
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

for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end='')
        else:
            print(' ', end='')
    print('')