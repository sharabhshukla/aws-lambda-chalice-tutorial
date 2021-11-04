from pydantic import BaseModel, constr, validator
from typing import Literal, List

class InputModel(BaseModel):
    Name: constr(max_length=50)
    Age: float
    Sex: str

    @validator('Sex')
    def sex_must_be(cls, v):
        allowed_sexes = ['Male', 'Female', 'Others']
        if v.title() not in allowed_sexes:
            raise ValueError('Sex must be {}'.format(allowed_sexes))
        return v.title()