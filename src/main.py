from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import db

app = FastAPI(title="Sample app")


@app.on_event("startup")
async def startup():
    db.init()

app.mount('/static', StaticFiles(directory=f'{Path(__file__).parent.parent}/static'), name='static')
