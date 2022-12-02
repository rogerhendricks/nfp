from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


###########  DEVICES ########
class DeviceIn(BaseModel):
    id: int
    manufacturer: str
    model: str
    dev_type: str
    hazard: Optional[bool] = False
    mri: Optional[bool] = False

    class Config:
        orm_mode = True


class Device(BaseModel):
    id: int
    manufacturer: str
    model: str
    dev_type: str
    hazard: Optional[bool] = False
    mri: Optional[bool] = False

    class Config:
        orm_mode = True


###########  LEADS #########
class LeadChamberEnum(str, Enum):
    atrium = 'Atrium'
    right_ventricle = 'Right Ventricle'
    left_ventricle = 'Left Ventricle'
    hb = 'His Bundle'
    lb = 'Left Bundle'


class LeadIn(BaseModel):
    id: int
    manufacturer: str
    model: str
    chamber: str
    hazard: Optional[bool] = False
    mri: Optional[bool] = False

    class Config:
        orm_mode = True


class Lead(BaseModel):
    id: int
    manufacturer: str
    model: str
    chamber: str
    hazard: Optional[bool] = False
    mri: Optional[bool] = False

    class Config:
        orm_mode = True

class DoctorIn(BaseModel):
    id: int
    title: str
    last_name: str
    first_name: str 
    phone: str
    email: str 
    street: str
    city: str 
    state: str 
    postal: str
    site_id: str


class Doctor(BaseModel):
    id: int
    title: str
    last_name: str
    first_name: str 
    phone: str
    email: str 
    street: str
    city: str 
    state: str 
    postal: str
    site_id: str