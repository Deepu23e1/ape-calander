from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    fullname: str
    username: str

class UserCreate(UserBase):
    password: str

    model_config = {"from_attributes": True} 

class UserOut(UserBase):
    id: int

    model_config = {"from_attributes": True}  