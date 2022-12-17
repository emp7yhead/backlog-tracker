from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserIn(UserBase):
    email: str


class UserOut(UserBase):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
