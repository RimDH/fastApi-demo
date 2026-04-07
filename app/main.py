from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes.user_routes import router as user_router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Routes
app.include_router(user_router, prefix="/users", tags=["Users"])

# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"}
    )