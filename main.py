from fastapi import FastAPI
from db import engine, Base
from controller import user_controller
from controller.user_controller import router as user_router
from sqlalchemy import text 

app = FastAPI(title="FastAPI Real-Time Project")
Base.metadata.create_all(bind=engine)  

@app.on_event("startup")
async def startup_event():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Database connected successfully!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

app.include_router(user_router)



