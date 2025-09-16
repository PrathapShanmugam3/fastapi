from fastapi import FastAPI
from api.v1.endpoints import user

app = FastAPI(title="FastAPI Real-Time Project")

app.include_router(user.router, prefix="/api/v1/user", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

