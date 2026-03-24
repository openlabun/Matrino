from fastapi import APIRouter
from src.schemas.v1.code import *
from src.api.v1.routes.code.core import *
from src.utils.general import response_wrapper

router = APIRouter()

@router.post('/code-to-generator')
def code_to_generator(data: LinealCode):
    return response_wrapper('Generator Matrix obtained',True,**generator_matrix(data.code, data.z))


@router.post('/lineal-code')
def lineal_code(data: GeneratorMatrix):
    return response_wrapper('Lineal code generated', True, **to_lineal_code(data.matrix, data.z) )

@router.post('/generator-to-control')
def control_matrix(data: ControlMatrix):
    return response_wrapper(
        'Control matrix obtained',
        True,
        **get_control_matrix(data.matrix, data.z, data.n)
        )

@router.post('/dual')
def dual_code(data: DualCode):
    return response_wrapper('Dual code generated', True, **to_dual(data.code, data.z))
