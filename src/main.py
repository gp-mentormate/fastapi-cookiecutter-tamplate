from pathlib import Path

from decouple import config
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import routers

app = FastAPI(
    title=config("APP_NAME", cast=str, default="FastAPI"),
    debug=config("DEBUG", cast=bool, default=False)
)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass


# Register static files folder path
app.mount(
    '/static',
    StaticFiles(directory=f'{Path(__file__).parent.parent}/static'),
    name='static'
)

# Register all application routers
for router in routers:
    app.include_router(router)
