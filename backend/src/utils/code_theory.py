from typing import List, Tuple
import sage.all as sage
import math

def get_finite_field(z):
    return sage.FiniteField(z)

def get_vector_space(field, n: int):
    return sage.VectorSpace(field, n)

def str_to_tuples(_list: List[str]) -> List[Tuple]:
    '''
        The function takes a list of strings and converts each element
        to a tuple. For example:
        Element: "0000" -> (0,0,0,0)
    '''
    return [tuple(map(int, string)) for string in _list]

def matrix_to_lists(matrix) -> List[list]:
    '''
        The functions takes a matrix and converts each row to a list. Returns
        a list of lists
    '''

    # Since each element it's an special type of integer (sage.rings.finite_rings.integer_mod.IntegerMod_int)
    # we need to convert it to a normal integer
    return [[int(x) for x in elem] for elem in  matrix.rows()]

def matrix_to_tuples(matrix: List) -> List[Tuple]:
    '''
        Takes a matrix and converts each row in a tuple. Returns
        a list of tuples
    '''
    return [tuple(elem) for elem in matrix]

def arr_to_string(a: List[tuple]) -> List[str]:
    return [''.join(map(str, elem)) for elem in a]

