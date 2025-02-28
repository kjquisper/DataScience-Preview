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
    
""" 
print(my_print("holamundo","soy"))
print(my_print())
 """


tab_string = "\t"

#print(len(tab_string))


first_name = "joel"
last_name = "mamani"

full_name = first_name + last_name
full_name2 = "{0} {1}".format(first_name,last_name)
full_name3 = f"{first_name} {last_name}"
#print(full_name3)


""" try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero") """


x = [0,1,2,3,5,6,7,8,9,10]

#print(x)
""" print(x[0])

x[0] = 11

print(x[0]) """

#print(x[1:8:7])

#para verificar si el elemento estan en la lista

#print(1 in x)


#extend debe ser en corchetes
#x.extend([12])

#print(x[-1])

empty_dic = {}
empty_dic2 = dict()

grades = {"joel":13, "pedro":15}

#print(grades["joel"])


#para evitar un exceperror podemos programar el mensaje que se mostrara cuando comentamos el erro

""" try:
    print(grades["kate"])
except:
    print("Kate no esta en el diccionario") """



joel_has_grade = "joel" in grades
kate_has_grade = "Kate" in grades
#print(joel_has_grade)
#print(kate_has_grade)


from collections import Counter

c = Counter([0, 1, 2, 0])
#print(c)

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for ‘else if’"
else:
    message = "when all else fails use else (if you want to)"


for x in range(10):
    if x == 3:
        continue
    if x ==5:
        break

    #print(x)


#x = None
#assert x = None

""" s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = "" """



#print(x)

# comprension de listas

even_numbers = [x for x in range(5) if x % 2 == 0] 
squares = [x * x for x in range(5)] 
even_squares = [x * x for x in even_numbers]




square_dict = {x: x*x for x in range(5)}
#print(square_dict)

#comprension de listas para conjuntos : la propiedad es que no tiene elementos repetidos
square_set = {x * x for x in [1,-2]}

#print(square_set)

#PRUEBAS AUTOMATIZADAS Y ASSERT
#-----------------------------------------------------------------------------------------------------------------------------

assert 1+1 == 2
assert 1+1 == 2, "1+1 should equal 2 but didn't "



def smallest_item(xs):
    return min(xs)#

#sirve para verificar que las fucnionesu operaciones hagan lo que se espera que hagan
assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1


def smallest_item(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)


#verificamos cons assert que la lista esta vacia , por lo que nos bota un error de assertion
""" df = [1,2,3,4]
dftst = []

assert df
assert dftst """

"""PROGRAMACION ORIENTADA A OBJETOS"""


class CountingCliker:
    def __init__(self, count = 0):
        self.count = count
        #print("estoy inciando el contador en: ",self.count)
    #
    def __repr__(self):
        return f"CountingClicker(count={self.count})"   
        
    def click(self, num_times =1):
        self.count+=num_times
        
    def read(self):
        return self.count
    
    def reset(self):
        self.count = 0
    
""" clicker1 = CountingCliker()
assert clicker1.read() == 0
clicker1.click()
clicker1.click()
clicker1.click()
assert clicker1.read() == 3 # "el contador deberia estar en 3"
print("el contador esta en: ",clicker1.read())
clicker1.reset()
assert clicker1.read() == 0 # luego de resetear , el contador debera estar en 0"
print("el contador ahora esta en ",clicker1.read())
#print(clicker1) """


class NoResetClicker(CountingCliker):
    def reset(self):
        pass
    

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1


"""ITERABLES Y GENERADORES"""

def generate_range(n):
    i = 0
    while i < n:
        yield i  # Se corrige `I` por `i`
        i += 1

""" for i in generate_range(10):
    print(f"i: {i}")  """

def natural_numbers():
    n = 1
    while True:
        #print(f"Yielding: {n}")  # Muestra el valor antes de yield
        yield n
        n += 1

# Iteramos sobre el generador
""" for num in natural_numbers():
    #print(f"Received: {num}")
    if num == 5:  # Detenemos después de 5 iteraciones para evitar un bucle infinito
        break """


evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)

#print(evens_below_20)

# Ninguno de estos cálculos *hace* nada hasta que iteramos
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# y así sucesivamente


""" for num in even_squares_ending_in_six:
    print(num)
    if num > 1000:  # Detenemos el bucle para evitar una iteración infinita
        break """
    
names = ["alice","bob","charlie","debbie"]

""" for i in range(len(names)):
    print(f"name {i}, in {names[i]}")
i = 0
 """
 
 
"""
for name in names:
    print(f"name {i} is {names[i]}")
    i += 1 """
    
"""     
for i,name in enumerate(names):
    print(f"name {i} is {name}") """
    
    
    
"""ALEATORIEDAD"""

import random
random.seed(10)
four_uniform_randoms = [random.random() for _ in range(4)]

#print(four_uniform_randoms)
""" 
random.seed(11)
print(random.random())
random.seed(11)
print(random.random()) """

#print(random.randrange(3,6))

""" up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)
print(random.choice(up_to_ten)) """

""" lottery_numbers = range(10,20)
winning_numbers = random.sample(lottery_numbers,2)

print(winning_numbers) """


"""EXPRESIONES REGULARES"""

import re
re_examples = [ # Todas son True, porque
not re.match("a", "cat"), # ‘cat’ no empieza por ‘a’
re.search("a", "cat"), # ‘cat’ contiene una ‘a’
not re.search("c", "dog"), # ‘dog’ no contiene una ‘c’.
3 == len(re.split("[ab]",
"carbs")),
"R-D-" == re.sub("[0-9]", "-",
"R2D2")
# Reemplaza dígitos por guiones.
]
#assert all(re_examples)

"""PROGRAMACION FUNCIONAL"""

"""EMPQUETADOS Y DESEMPAQUETADOS DE ARGUMENTOS"""

list1 = ['a', 'b', 'c']
list2 = [1,2,3]

[print(pair) for pair in zip(list1, list2)] 

