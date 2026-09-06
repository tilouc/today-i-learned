#OOP
#class

# 4 pillars of oop: 
# encapsulation
# abstraction
# inheritance
# polymorphism

class BigObject: #Class or Blueprint
    #code
    pass

obj1 = BigObject() #Object or Instance
obj2 = BigObject()
obj3 = BigObject()

print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))
print(type(BigObject))
print(type(obj1))


"""
class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name='anonymous', age=0):
        # if (self.membership):#or PlayerCharacter.membership
        if (age > 18):
            self.name = name #attributes or properties
            self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'my name is {self.name}')
"""


# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 21)
# player1 = PlayerCharacter()
# player2 = PlayerCharacter()
# player1 = PlayerCharacter('Tom', 10)
# player2 = PlayerCharacter()

# player2.attack = 50

# print(player1.name)
# print(player1.age)
# print(player1.run())
# print(player2.name)
# print(player2.age)
# print(player1)
# print(player2)
# print(player1.attack)
# print(player2.attack)

# help(player1)
help(list)

# print(player1.membership)
# print(player2.membership)

# print(player1.name)

# print(player1.shout())
# print(player2.shout())


# Exercise: Cats Everywhere

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats



# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

def oldest_cat(*args: int):
    return 'The oldest cat is {max(*args)}'

cat1 = Cat('blacky1', 6)
cat2 = Cat('blacky2', 7)
cat3 = Cat('blacky3', 8)

oldest_cat(cat1.age, cat2.age, cat3.age)


class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Tom', 20)

# print(player1.shout())
# print(player1.adding_things(2,3))

# print(PlayerCharacter.adding_things(2,3))

player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)


class NameOfClass():
    class_attribute = 'value'
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        #code
    
    @classmethod
    def cls_method(cls, param1, param2):
        #code
    
    @staticmethod
    def stc_method(param1, param2):
        #code


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return self

# player1 = PlayerCharacter('andrei', 100)
print(player1.run())


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and i am {self.age} years old')

player1 = PlayerCharacter('andrei', 100)
player1.speak()
print(player1.name)
print(player1.age)

player2 = {'name': 'andrei', 'age': 100}
print(player2['name'])
print(player2['age'])


player1 = PlayerCharacter('andrei', 100)
player1.speak()
print((1,2,3,1).count(1))
print(len((1,2,3,1)))
camera.takepicture()

player1.name = '!!!'
player1.speak = 'BOOOO'

print(player1.speak)


class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print(f'my name is {self._name}, and i am {self._age} years old')

player1 = PlayerCharacter('andrei', 100)
# player1.name = '!!!'
# player1.speak = 'BOOOO'

print(player1.speak())


#users
# - Wizards
# - Archers
# - Ogres
class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)

print(wizard1)
print(wizard1.sign_in())

print(wizard1.attack())
print(archer1.attack())

wizard1 = Wizard('Merlin', 60)
# isinstance(instance, Class)
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))


print(wizard1.attack)
print(archer1.attack)

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()

print(wizard1.attack())