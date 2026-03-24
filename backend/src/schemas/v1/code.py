from pydantic import BaseModel

# Lineal Code endpoint
class GeneratorMatrix(BaseModel):
    z: int
    matrix: list[list[int]]

# Code to Generator matrix endpoint
class LinealCode(BaseModel):
    z: int
    code: list[str]

# Generator to Control Matrix endpoint
class ControlMatrix(BaseModel):
    n: int
    z: int
    matrix: list[list[int]]

# Dual code endpoint
class DualCode (BaseModel):
    z: int
    code: list[str]
