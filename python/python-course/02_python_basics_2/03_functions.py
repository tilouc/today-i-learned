# functions
# DRY
def say_hello():
    print('hello')

say_hello()

def show_tree(picture):
    for image in picture:
        for pixel in image:
            if (pixel):
                print('*',end='')
            else:
                print(' ',end='')
        print('')

show_tree([
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
])
show_tree([
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
])
show_tree([
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
])

#parameters
def say_hello(name, emoji):
    print(f'hello {name} {emoji}')

# positional arguments
say_hello('tilou', '☺️') #call, invoke
say_hello('daniel', '☺️')
say_hello('emilie', '☺️')

# keyword arguments
# say_hello(emoji='☺️', name='bibi') # bad practice
say_hello(name='bibi', emoji='☺️')

# default parameters
def say_hello(name='darth vader', emoji='😈'):
    print(f'hello {name} {emoji}')

say_hello()
say_hello('timmy')

# return

def sum(num1, num2):
    return num1 + num2

# a function should:
# do one thing really well.
# return something.
# good practice

# print(sum(4,5))
# print(sum(10,5))
total = sum(10,5) # 15
print(sum(10,total))
print(sum(10,15))
print(sum(10,sum(10,5)))

def sum(num1,num2):
    def another_funct(n1,n2):
        return n1 + n2
    return another_funct(num1,num2)
    # return automatically exits the function


total = sum(10,20)
print(total)

# exercise tesla

age = input("What is your age?: ")

if int(age) < 18:
	print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
	print("Powering On. Enjoy the ride!");
elif int(age) == 18:
	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriveAge(age=0):

    if int(age) < 18:
        return "Sorry, you are too young to drive this car. Powering off"
    elif int(age) > 18:
        return "Powering On. Enjoy the ride!"
    elif int(age) == 18:
        return "Congratulations on your first year of driving. Enjoy the ride!"

print(checkDriveAge(20))

# methods vs functions
# list()
# print()
# max()
# min()
# input()

def some_random_stuff():
    pass

some_random_stuff() # a function

method = 'hello'.capitalize() # a method
print(method)

# print vs print + return + return

def test(a):
    print(a)

def test2(a):
    print(a)
    return a

def test3(a):
    return a

x = test(10)
y = test2(10)
z = test3(10)

print("x =", x)
print("y =", y)
print("z =", z)

#docstrings

def test(a):
    '''
    info: this function tests and prints param a
    '''
    print(a)

test('!!!!')
# test()
help(test)
print(test.__doc__)
# len()

# clean code
def is_even(num):
    return num % 2 == 0
    # if num % 2 == 0:
        # return True
    # return False
    # else:
        # return False

print(is_even(50))
print(is_even(51))

# args and kwargs
# *args **kwargs

def super_func(name, *args, i='hi', **kwargs):
    # print(*args)
    # print(args)
    # print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func('tilou', 1,2,3,4,5, num1=5, num2=10))

#Rule: params, *args, default parameters, **kwargs

def calculate_order(customer_name, *args, discount=15, **kwargs):
    discount_price = int(((sum(args) * discount) / 100))
    total = 0
    for item in kwargs.values():
        total += item
    
    return sum(args) - discount_price + total

print(calculate_order('tilou', 10,20,30, item1=12,item2=15))

# exercise functions

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)

    return max(evens)

print(highest_even([2,10,2,3,4,8,11]))

# walrus operator
a = 'hellooooooo'

if ((n := len(a)) > 10):
    print(f"too long {n} elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)