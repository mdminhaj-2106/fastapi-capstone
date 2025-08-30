from fastapi import FastAPI
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handler


app = FastAPI(title='Car Price Prediction App')

# Link Middleware
app.add_middleware(LoggingMiddleware)

#link endpoints
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags=['Predict'])


#Error Handling
register_exception_handler(app)