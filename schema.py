from datetime import date
from pydantic import BaseModel

class region(BaseModel):

    id = int
    nombre_region = str
    created_at = date

    class Config:
        orm_mode = True