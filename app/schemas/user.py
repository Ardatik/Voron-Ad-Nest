from pydantic import BaseModel, Field, EmailStr, field_validator
from uuid import UUID
from typing import Optional
from datetime import date
import re


class UserRegister(BaseModel):
    username: str = Field(
        min_length=6, max_length=16, description="username пользователя"
    )
    email: EmailStr = Field(description="email пользователя")
    phone_number: str = Field(description="телефон пользователя")
    password: str = Field(
        min_length=8, max_length=20, description="Пароль пользователя"
    )
    first_name: str = Field(min_length=2, max_length=16, description="Имя пользователя")
    last_name: str = Field(
        min_length=2, max_length=20, description="Фамилия пользователя"
    )
    patronymic_name: Optional[str] = Field(
        default=None, min_length=2, max_length=20, description="Отчество пользователя"
    )
    date_of_birth: date = Field(description="Дата рождения пользователя")

    @field_validator("phone_number", mode="before")
    @classmethod
    def validate_phone_number(cls, phone: str) -> str:
        pattern = r"^\+?[1-9][0-9]{7,14}$"
        if not re.match(pattern, phone):
            raise ValueError("Неверный формат номера телефона")
        return phone

    @field_validator("date_of_birth", mode="before")
    @classmethod
    def validate_date_of_birth(cls, birth_date: date) -> date:
        if birth_date > date.today():
            raise ValueError("Неверно указана дата рождения")
        if (date.today() - birth_date).days / 365 < 14:
            raise ValueError("Возраст должен быть не менее 14 лет")
        return birth_date


class UserLogin(BaseModel):
    username: Optional[str] = Field(
        default=None, min_length=6, max_length=16, description="username пользователя"
    )
    email: Optional[EmailStr] = Field(default=None, description="email пользователя")
    phone_number: Optional[str] = Field(
        default=None, description="телефон пользователя"
    )
    password: str = Field(min_length=8, description="Пароль пользователя")


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    phone_number: str
    first_name: str
    last_name: str
    patronymic_name: Optional[str]
    date_of_birth: date
    is_active: bool

    class Config:
        from_attributes = True


class ChangeAccountData(BaseModel):
    pass
