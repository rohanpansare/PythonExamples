name = "Rohan"
subject = "Treehouse loves {}"
print(subject.format(name))

my_list = [1,2,3,4,5]
my_list.append(6)
print(my_list)
my_list.append([7,8])
my_list.extend([7,6,3,2])
print(my_list)
my_list.remove([7,8])
print(my_list)
print(list("hello"))
alpha = 'abcdea'
print(alpha.index('a'))
list1 = (list(alpha))
del list1[0]
alpha = "".join(list1)
print (alpha)

if not 'r'  in alpha:
    print("Not present "*4)
else:
    print("Present")*2

list1 = [1,2,3]*4
print (list1)

def add(num1,num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return None
    else:
        return num1+num2

    def loopy(items):
        # Code goes here
        for item in items:
            if item == "STOP":
                break
            print(item)

from random import *

secret_num = randint(1,10)

def just_right(string):
    if len(string) < 5 :
        print("Your string is too short")
    elif len(string) > 5 :
        print("Your string is too long")
    else :
        return True

print(just_right("hell"))

def squared(val):
    try :
        val = int(val)
    except ValueError :
        return val*len(val)
    else :
        return val**2

import random

def even_odd(num):
    if num%2 == 0:
        return num%2
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2

start = 5
while start:
    num = random.randint(1,99)
    if even_odd(num):
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
    start -= 1

our_list = list(range(0,10))
print(our_list)
