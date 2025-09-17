import logging
import sys
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from db.db import create_db_and_tables
from endpoints.task import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router, prefix="/tasks")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    uvicorn.run("main_api:app", host="0.0.0.0", port=8000, reload=True)
