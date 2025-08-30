from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

def register_exception_handler(app: FastAPI):
    @app.add_exception_handler(Exception)
    async def custom_exception_handler(req: Request, ex: Exception):
        return JSONResponse(status_code=500, content={'detail': str(ex)}) 