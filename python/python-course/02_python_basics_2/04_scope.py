# scope - what variables do i have access to?

# print(name) # not defined

if True:
    x = 10

def some_func():
    total = 100

print(total)
print(x)

# guess the output

a = 1
def parent():
    # a = 10
    def confusion():
        # a = 5
        # return a
        return sum
    return confusion()

# print(a)
# print(confusion())
# print(confusion())
print(parent())
print(a)

#1 - start with local
#2 - parent local?
#3 - global
#4 - built in python functions.

# global keyword

a = 10
def confusion(b):
    print(b)
    # a = 90

confusion(300)

total = 0

def count(total):
    # global total
    total += 1
    return total

# count(total)
# count(total)
print(count(count(count(total)))) # 3
# print(count(count(1))) # 3
# print(count(2)) # 3
# print(3) # 3

# nonlocal keyword

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    x = "fuck"
    print("outer:", x)
    inner()

outer()