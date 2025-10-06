from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Uuid, Float, DateTime, ForeignKey, func
import uuid
from .base import Base
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .account import User


class Category(Enum):
    service = "service"
    product = "product"
    company = "company"


class Platforms(Enum):
    yandex = "yandex"
    avito = "avito"


class Advertisement(Base):
    __tablename__ = "advertisement"

    adv_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4, index=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("users.id"), nullable=False
    )
    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default=lambda: f"Реклама от {datetime.now().strftime('%Y%m%d%H%M')}",
    )
    type_service: Mapped[Category]
    platforms: Mapped[Platforms]
    adv_text: Mapped[str] = mapped_column(String, nullable=False)
    status_paid: Mapped[bool] = mapped_column(Boolean, server_default="true")
    price: Mapped[float] = mapped_column(Float, nullable=False)
    date_create_adv: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    date_start_adv: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    date_finish_adv: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_active_adv: Mapped[bool] = mapped_column(Boolean, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="advertisements")
