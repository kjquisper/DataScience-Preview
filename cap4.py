"""ALGEBRA LINEAL"""


from typing import List

Vector = List[float]

height_weight_age = [70,170,40]
#pulgadas
#libras
#años
grades = [95,80,75,62]

#suma de 2 vectores

def add(v:Vector, w:Vector) -> Vector:
    """agregamos los elementos"""
    assert len(v) ==len(w)
    return [v_i + w_i for v_i,w_i in zip(v,w)]
assert add([1,3,4],[3,1,0]) == [4,4,4]

#diferencia de vectores

def subtract(v: Vector, w: Vector) -> Vector:
    """restamos los elementos correspondientes"""
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

#suma de varios vectores

def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    # Comprueba que los vectores no estén vacíos
    assert vectors, "no vectors provided!"
    # Comprueba que los vectores tienen el mismo tamaño
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    # el elemento i del resultado es la suma de cada vector [i]
    return [sum(vector[i] for vector in vectors)
    for i in range(num_elements)]
assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

#multi0plicacion de un vector por un escalar

def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]
assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

# calcula la media de una lista de vectores

def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]



"""PRODUCTO PUNTO"""


def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
assert dot([1, 2, 3], [4, 5, 6]) == 32 # 1 * 4 + 2 * 5 + 3 * 6


#suma de cuadrados

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)
assert sum_of_squares([1, 2, 3]) == 14 # 1 * 1 + 2 * 2 + 3 * 3



import math

def magnitude(v: Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))
assert magnitude([3, 4]) == 5
#9+16 = 25

def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1–w_1) ** 2 + ... + (v_n–w_n) ** 2"""
    return sum_of_squares(subtract(v, w))

def distance(v: Vector, w: Vector) -> float:
    """Computes the distance between v and w"""
    return math.sqrt(squared_distance(v, w))



