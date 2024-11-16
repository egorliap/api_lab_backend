from fastapi import FastAPI

from .exchange.router import router as exchange_router


app = FastAPI(tags=["Exchange service"])

@app.get("/", tags=["Home"])
async def home():
    return {"message": "Hello world!"}

app.include_router(exchange_router)