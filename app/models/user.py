from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, Uuid, Date
import uuid
from .base import Base
from typing import List, Optional, TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from .advertisiment import Advertisement


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4, index=True
    )
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    patronymic_name: Mapped[Optional[str]] = mapped_column(String(40), nullable=True)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, server_default="true")

    advertisements: Mapped[List["Advertisement"]] = relationship(
        "Advertisement", back_populates="user"
    )
