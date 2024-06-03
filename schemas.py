from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DataResponse(BaseModel):
    timestamp: datetime
    wind_speed: Optional[float]
    power: Optional[float]
    ambient_temperature: Optional[float]

    class Config:
        orm_mode = True
