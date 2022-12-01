from typing import List
from pydantic import BaseModel


class DeviceIn(BaseModel):
    id: int
    manufacturer: str
    model: str
    dev_type: str
    hazard: bool
    mri: bool


class Device(BaseModel):
    id: int
    manufacturer: str
    model: str
    dev_type: str
    hazard: bool
    mri: bool