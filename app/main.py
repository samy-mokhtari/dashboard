from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import init_db
from app.routes import dashboard

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(dashboard.router)

templates = Jinja2Templates(directory="app/templates")

init_db()