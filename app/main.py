from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.dependencies.containers import Container
from app.api.routes import chat, ecommerce

templates = Jinja2Templates(directory="app/templates")


def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=[ecommerce, chat])
    app = FastAPI()
    app.container = container
    app.include_router(chat.router)
    app.include_router(ecommerce.router)
    return app


app = create_app()


@app.get("/", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})
