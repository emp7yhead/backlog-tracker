from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
