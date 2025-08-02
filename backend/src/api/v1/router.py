from fastapi import APIRouter
from src.api.v1.routes.code import endpoints as code_theory
from src.api.v1.routes.discrete import endpoints as discrete_math

router = APIRouter()

# Endpoints for discrete math and code theory
router.include_router(code_theory.router, prefix='/code-theory')
router.include_router(discrete_math.router, prefix='/discrete-math')
