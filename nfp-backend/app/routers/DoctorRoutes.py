from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.sql import text

from ..database import users, doctors, database
from ..models import Doctor, DoctorIn

router = APIRouter(
    prefix="/doctors"
)

@router.get("/", response_model=List[Doctor])
async def read_doctors():
    query = doctors.select()
    return await database.fetch_all(query)


@router.post("/create", response_model=Doctor)
async def create_doctor(doctor: DoctorIn):
    query = doctors.insert().values(
        id=doctor.id,
        title=doctor.title, 
        last_name=doctor.last_name, 
        first_name=doctor.first_name, 
        phone=doctor.phone,
        email=doctor.email,
        street=doctor.street,
        city=doctor.city,
        state=doctor.state,
        postal=doctor.postal,
        site_id=doctor.site_id,
        )
    last_record_id = await database.execute(query)
    return {**doctor.dict(), "id": last_record_id}


@router.get("/{id}")
async def read_doctor(id: int):
    query = doctors.select().where(doctors.c.id == text(str(id)))
    return await database.fetch_one(query)


@router.delete("/{id}")
async def delete_doctor(id: int, doctor: Doctor):
    value =  doctors.delete().where(doctors.c.id == text(str(id)))
    return await database.execute(value)


@router.patch("/{id}", response_model=Doctor)
async def update_doctor(id:int, doctor: DoctorIn):
    print(doctor)
    query = doctors.update().values(
        id=doctor.id,
        title=doctor.title, 
        last_name=doctor.last_name, 
        first_name=doctor.first_name, 
        phone=doctor.phone,
        email=doctor.email,
        street=doctor.street,
        city=doctor.city,
        state=doctor.state,
        postal=doctor.postal,
        site_id=doctor.site_id,
        ).where(doctors.c.id == text(str(id)))
    await database.execute(query)
    return  doctors