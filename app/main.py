from fastapi import FastAPI

from app.api.routes import chat, ecommerce

app = FastAPI()

app.include_router(chat.router)
app.include_router(ecommerce.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
