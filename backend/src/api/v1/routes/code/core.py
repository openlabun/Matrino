from typing import List
from src.utils.code_theory import *
import sage.all as sage

def generator_matrix(code: List[str], z: int) -> dict:

    n = len(code[0]) # 'n' is the code longitude

    field = get_finite_field(z)
    space = get_vector_space(field, n)

    # This converts each element of the code that comes as a string (e.g '10100')
    # to a list of ints and then parses it as a tuple
    elems = str_to_tuples(code)

    lineal_code = space.subspace(elems)

    k = int(lineal_code.dimension())

    # The generator matrix is composed of the bases of the field
    raw_matrix = sage.matrix(lineal_code.basis())

    # In order to be able to send it in a JSON, we need to parse it
    generator_matrix = matrix_to_lists( raw_matrix )

    return {'matrix': generator_matrix, 'n': n, 'k': k}

def to_lineal_code(matrix: List[List[int]], z: int) -> dict:

    n = len(matrix[0])

    field = get_finite_field(z)
    space = get_vector_space(field, n)

    basis = matrix_to_tuples(matrix)

     # Here there are all the elements of the linear code
    raw_code = space.subspace(basis)

    # However, we need to parse them as a list of strings
    codewords = arr_to_string(raw_code)

    # With this we can get 'k'
    k = int(raw_code.dimension())

    return {'codewords': codewords, 'n': n, 'k': k}

def get_control_matrix(matrix: List[List[int]], z: int, n: int) -> dict:
    '''
    Given a generator matrix it returns the corresponding control matrix
    '''

    field = get_finite_field(z)
    space = get_vector_space(field, n)

    # This step is needed because sage.matrix receives a list
    # of tuples
    basis = matrix_to_tuples(matrix)

    raw_control_matrix = sage.matrix(field,basis).\
        right_kernel().\
        matrix()

    matrix_control = matrix_to_lists( raw_control_matrix )

    return {'matrix': matrix_control}

def to_dual(code: List[str], z: int) -> dict:

   n = len( code[0] )

   G = generator_matrix(code, z)['matrix']

   control_matrix = get_control_matrix(G, z, n )['matrix']

   basis = matrix_to_tuples(control_matrix)

   space = get_vector_space(get_finite_field(z), n)

   raw_dual = space.subspace(basis)

   dual = arr_to_string(raw_dual)

   return {'dual': dual}




