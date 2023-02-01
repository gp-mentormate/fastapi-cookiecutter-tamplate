from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from sample_app.routes import router as sample_app_router
from database import db

app = FastAPI(title="Sample app")


@app.on_event("startup")
async def startup():
    db.init()
    await db.create_all()


common_prefix = '/api'
app.include_router(sample_app_router, prefix=common_prefix)
app.mount('/static', StaticFiles(directory=f'{Path(__file__).parent.parent}/static'), name='static')
