from pydantic import BaseModel


class InputModel(BaseModel):
    value: int


class OutputModel(BaseModel):
    result: int
