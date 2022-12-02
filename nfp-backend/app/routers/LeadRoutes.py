from fastapi import Depends, APIRouter, HTTPException, status
from typing import List


from ..database import users, devices, leads, database
from ..models import Lead, LeadIn

router = APIRouter(
    prefix="/leads"
)

@router.get("/", response_model=List[Lead])
async def read_leads():
    query = leads.select()
    return await database.fetch_all(query)


@router.post("/create", response_model=Lead)
async def create_lead(lead: LeadIn):
    query = leads.insert().values(
        manufacturer=lead.manufacturer, 
        model=lead.model, 
        chamber=lead.chamber, 
        hazard=lead.hazard,
        mri=lead.mri,
        )
    last_record_id = await database.execute(query)
    return {**lead.dict(), "id": last_record_id}


@router.get("/{id}")
async def read_lead(id: int):
    query = leads.select().where(leads.c.id == text(str(id)))
    return await database.fetch_one(query)


@router.delete("/{id}")
async def delete_lead(id: int, lead: Lead):
    value =  leads.delete().where(leads.c.id == text(str(id)))
    return await database.execute(value)


@router.patch("/{id}", response_model=Lead)
async def update_device(id:int, lead: LeadIn):
    print(lead)
    query = leads.update().values(
        id=lead.id,
        manufacturer=lead.manufacturer, 
        model=lead.model, 
        chamber=lead.chamber, 
        hazard=lead.hazard,
        mri=lead.mri,
        ).where(leads.c.id == text(str(id)))
    await database.execute(query)
    return  lead
