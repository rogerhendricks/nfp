import os
import databases
import sqlalchemy
from typing import List
from fastapi import FastAPI, status
# from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.sql import text

from .database import database, devices
from .models import Device, DeviceIn


app = FastAPI()

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


##############   Devices CRUD  #################
@app.get("/devices/", response_model=List[Device])
async def read_devices():
    query = devices.select()
    return await database.fetch_all(query)


@app.post("/devices/", response_model=Device)
async def create_device(device: DeviceIn):
    query = devices.insert().values(
        manufacturer=device.manufacturer, 
        model=device.model, 
        dev_type=device.dev_type, 
        hazard=device.hazard,
        mri=device.mri,
        )
    last_record_id = await database.execute(query)
    return {**device.dict(), "id": last_record_id}


@app.get("/devices/{id}")
async def read_device(id: int):
    query = devices.select().where(devices.c.id == text(str(id)))
    return await database.fetch_one(query)


@app.delete("/devices/{id}")
async def delete_device(id: int, device: Device):
    value =  devices.delete().where(devices.c.id == text(str(id)))
    return await database.execute(value)


@app.patch("/device/{id}", response_model=Device)
async def update_device(id:int, device: DeviceIn):
        print(id)
        query = devices.update().values(
        id=device.id,
        manufacturer=device.manufacturer, 
        model=device.model, 
        dev_type=device.dev_type, 
        hazard=device.hazard,
        mri=device.mri,
        ).where(devices.c.id == text(id))
        print(query)
        return await database.execute(query)