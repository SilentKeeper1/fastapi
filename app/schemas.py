from pydantic import BaseModel, field_validator

class AnimalResponse(BaseModel):
    id: int
    name: str
    age: int
    adopted: bool

    @field_validator('age')
    def validate_age(cls, v):
        if v < 0:
            raise ValueError('age cannot be negative')
        return v

    class Config:
        orm_mode = True