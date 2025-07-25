from fastapi import FastAPI
from routes.rutes import routes
from config.db import engine,base

base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(routes)