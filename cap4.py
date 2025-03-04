"""ALGEBRA LINEAL"""


from typing import List

Vector = List[float]

height_weight_age = [70,170,40]
#pulgadas
#libras
#años
grades = [95,80,75,62]

def add(v:Vector, w:Vector) -> Vector:
    """agregamos los elementos"""
    assert len(v) ==len(w)
    return [v_i + w_i for v_i,w_i in zip(v,w)]
assert add([1,3,4],[3,1,0]) == [4,4,4]

def subtract(v: Vector, w: Vector) -> Vector:
    """restamos los elementos correspondientes"""
    assert len(v) == len(w)
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
