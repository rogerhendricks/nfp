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



app = FastAPI()

app.include_router(DoctorRoutes.router)
app.include_router(DeviceRoutes.router)
app.include_router(LeadRoutes.router)

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
# @app.get("/devices/", response_model=List[Device])
# async def read_devices():
#     query = devices.select()
#     return await database.fetch_all(query)


# @app.post("/devices/", response_model=Device)
# async def create_device(device: DeviceIn):
#     query = devices.insert().values(
#         manufacturer=device.manufacturer, 
#         model=device.model, 
#         dev_type=device.dev_type, 
#         hazard=device.hazard,
#         mri=device.mri,
#         )
#     last_record_id = await database.execute(query)
#     return {**device.dict(), "id": last_record_id}


# @app.get("/devices/{id}")
# async def read_device(id: int):
#     query = devices.select().where(devices.c.id == text(str(id)))
#     return await database.fetch_one(query)


# @app.delete("/devices/{id}")
# async def delete_device(id: int, device: Device):
#     value =  devices.delete().where(devices.c.id == text(str(id)))
#     return await database.execute(value)


# @app.patch("/device/{id}", response_model=Device)
# async def update_device(id:int, device: DeviceIn):
#     print(device)
#     query = devices.update().values(
#         id=device.id,
#         manufacturer=device.manufacturer, 
#         model=device.model, 
#         dev_type=device.dev_type, 
#         hazard=device.hazard,
#         mri=device.mri,
#         ).where(devices.c.id == text(str(id)))
#     await database.execute(query)
#     return  device

##############   Leads CRUD  #################
# @app.get("/leads/", response_model=List[Lead])
# async def read_leads():
#     query = leads.select()
#     return await database.fetch_all(query)


# @app.post("/leads/", response_model=Lead)
# async def create_lead(lead: LeadIn):
#     query = leads.insert().values(
#         manufacturer=lead.manufacturer, 
#         model=lead.model, 
#         chamber=lead.chamber, 
#         hazard=lead.hazard,
#         mri=lead.mri,
#         )
#     last_record_id = await database.execute(query)
#     return {**lead.dict(), "id": last_record_id}


# @app.get("/leads/{id}")
# async def read_lead(id: int):
#     query = leads.select().where(leads.c.id == text(str(id)))
#     return await database.fetch_one(query)


# @app.delete("/leads/{id}")
# async def delete_lead(id: int, lead: Lead):
#     value =  leads.delete().where(leads.c.id == text(str(id)))
#     return await database.execute(value)


# @app.patch("/leads/{id}", response_model=Lead)
# async def update_device(id:int, lead: LeadIn):
#     print(lead)
#     query = leads.update().values(
#         id=lead.id,
#         manufacturer=lead.manufacturer, 
#         model=lead.model, 
#         chamber=lead.chamber, 
#         hazard=lead.hazard,
#         mri=lead.mri,
#         ).where(leads.c.id == text(str(id)))
#     await database.execute(query)
#     return  lead