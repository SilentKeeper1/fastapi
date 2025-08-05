from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from datetime import date
import re


class User(BaseModel):
    full_name: str = Field(..., min_length=5)
    email: EmailStr
    age: int = Field(..., ge=18, le=120)
    password: str
    phone: str
    birth_date: date

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if value.endswith("@example.com"):
            raise ValueError("Email не може бути з доменом example.com")
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Пароль має бути щонайменше 8 символів")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Пароль має містити хоча б одну велику літеру")
        if not re.search(r"\d", value):
            raise ValueError("Пароль має містити хоча б одну цифру")
        if not re.search(r"[^\w\s]", value):
            raise ValueError("Пароль має містити хоча б один спецсимвол")
        return value

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        if not re.fullmatch(r"\+380\d{9}", value):
            raise ValueError("Телефон має бути у форматі +380XXXXXXXXX")
        return value

    @model_validator(mode="after")
    def validate_birth_date_matches_age(self) -> "User":
        today = date.today()
        calculated_age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        if self.age != calculated_age:
            raise ValueError(f"Вік ({self.age}) не відповідає даті народження ({self.birth_date})")
        return self
