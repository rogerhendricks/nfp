from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.sql import text

from ..database import users, devices, database
from ..models import Device, DeviceIn

router = APIRouter(
    prefix="/devices"
)

@router.get("/", response_model=List[Device])
async def read_devices():
    query = devices.select()
    return await database.fetch_all(query)


@router.post("/create", response_model=Device)
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


@router.get("/{id}")
async def read_device(id: int):
    query = devices.select().where(devices.c.id == text(str(id)))
    return await database.fetch_one(query)


@router.delete("/{id}")
async def delete_device(id: int, device: Device):
    value =  devices.delete().where(devices.c.id == text(str(id)))
    return await database.execute(value)


@router.patch("/{id}", response_model=Device)
async def update_device(id:int, device: DeviceIn):
    print(device)
    query = devices.update().values(
        id=device.id,
        manufacturer=device.manufacturer, 
        model=device.model, 
        dev_type=device.dev_type, 
        hazard=device.hazard,
        mri=device.mri,
        ).where(devices.c.id == text(str(id)))
    await database.execute(query)
    return  device