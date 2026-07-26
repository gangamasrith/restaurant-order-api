from fastapi import FastAPI
from database import Base, engine
from routers.orders import router as orders_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Restaurant Order API",
    description="Fullstack Developer Assessment API",
    version="1.0.0"
)

app.include_router(orders_router)


@app.get("/")
def home():
    return {
        "message": "Restaurant Order API is Running Successfully!"
    }
