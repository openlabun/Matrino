from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1 import router as v1_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers for versions
app.include_router(v1_router.router, prefix='/v1')

@app.get('/health')
def health():
    return {'health': 'Matrino is healthy!'}

# Exceptions handlers

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={'success': False, 'message': exc.detail}
    )

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={'success': False, 'message': 'An unknown error happened. Try later'}
    )
