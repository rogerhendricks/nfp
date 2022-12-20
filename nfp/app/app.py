import os
import databases
import sqlalchemy
from typing import List
from fastapi import FastAPI, status
# from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.sql import text

from .routers import LeadRoutes, DeviceRoutes, DoctorRoutes
from .database import database

from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(DoctorRoutes.router)
app.include_router(DeviceRoutes.router)
app.include_router(LeadRoutes.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
