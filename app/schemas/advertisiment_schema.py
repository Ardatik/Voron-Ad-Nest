from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from enum import Enum
from voron.app.models.advertisiment import Category, Platforms
from datetime import datetime

class Advertisiment(BaseModel):
    adv_id: UUID
    user_id: UUID
    title: str
    type_service: Category
    platforms: Platforms
    price: float
    date_start_adv: datetime
    date_finish_adv: datetime
    is_active_adv: bool
    
