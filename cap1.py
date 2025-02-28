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

