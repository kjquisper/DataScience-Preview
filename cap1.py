""" for i in [1,2,3,4,5]:
    print(i)
    for j in [1,2,3,4,5]:
        print(j)
        print(j+i)
    print(i)
print("done looping") """



""" two_plus_three = 2 * 3
                
                
print(two_plus_three) """

""" for i in [1, 2, 3, 4, 5]:
# observe la línea en blanco
    print(i) """
    
#MODULOS EN PYTHON


""" import re
my_regex = re.compile("[0-9]+",re.I)

import re as regex
my_regex = regex.compile("[0-9]+", regex.I) """


""" match = 10
import re as regex

print(regex.match)
print(match) """


def double(x):
    return x*2


def apply_to_one(f):
    return f(1)
my_double = double

x = apply_to_one(my_double)
#print(x)


y = apply_to_one(lambda x:x+4)  # es igual a 5


#print(y)


suma = lambda x, y: x + y
#print(suma(3, 5))  # Salida: 8


def my_print(message = "mi mensaje 1",mmsd = "mi mensaje 2"):
    #print(message)
    return message + mmsd
    

print(my_print("holamundo","soy"))
print(my_print())