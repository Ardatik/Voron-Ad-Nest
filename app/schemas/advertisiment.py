from pydantic import BaseModel, model_validator, Field
from uuid import UUID
from typing import Optional
from enum import Enum
from datetime import datetime


class Category(str, Enum):
    service = "service"
    product = "product"
    company = "company"


class Platforms(str, Enum):
    yandex = "yandex"
    avito = "avito"


class AdvertisimentCreate(BaseModel):
    title: str = Field(
        ..., min_length=1, max_length=200, description="Заголовок рекламы"
    )
    type_service: Category
    platforms: Platforms
    adv_text: str
    price: float = Field(..., gt=0, description="Цена рекламы")
    date_start_adv: datetime
    date_finish_adv: datetime

    @model_validator(mode="after")
    def validate_dates(self):
        if self.date_start_adv >= self.date_finish_adv:
            raise ValueError("Дата окончания рекламы должна быть позже даты начала")
        return self


class AdvertisimentUpdate(BaseModel):
    title: Optional[str] = Field(
        None, min_length=1, max_length=200, description="Заголовок рекламы"
    )
    type_service: Optional[Category] = None
    platforms: Optional[Platforms] = None
    price: Optional[float] = Field(None, gt=0, description="Цена рекламы")
    date_start_adv: Optional[datetime] = None
    date_finish_adv: Optional[datetime] = None

    @model_validator(mode="after")
    def validate_dates(self):
        if (
            self.date_start_adv
            and self.date_finish_adv
            and self.date_start_adv >= self.date_finish_adv
        ):
            raise ValueError("Дата окончания рекламы должна быть позже даты начала")
        return self


class AdvertisimentResponse(BaseModel):
    adv_id: UUID
    user_id: UUID
    title: str
    type_service: Category
    platforms: Platforms
    price: float
    date_start_adv: datetime
    date_finish_adv: datetime
    is_active_adv: bool
