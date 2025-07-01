from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    score: float

    class Config:
        orm_mode = True
