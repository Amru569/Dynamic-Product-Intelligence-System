from fastapi import FastAPI

from app.database import Base, engine
from app.models import Product
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Dynamic Product Intelligence Platform",
    description="Upload and analyze Product/Inventory Catalog datasets.",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {

        "status": "success",

        "application": "Dynamic Product Intelligence Platform",

        "version": "1.0.0"

    }