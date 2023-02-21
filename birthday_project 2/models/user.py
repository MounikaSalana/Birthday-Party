from pydantic import BaseModel

class userdatamodel(BaseModel):
    name:str
    year:int
    month:int
    date:int