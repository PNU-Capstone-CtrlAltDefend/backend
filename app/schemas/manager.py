# schemas/manager.py
from pydantic import BaseModel, EmailStr

class ManagerSignup(BaseModel):
    id: str
    name: str
    email: EmailStr
    password: str
    phone: str
    organization_name: str

class ManagerLogin(BaseModel):
    email: EmailStr
    password: str
