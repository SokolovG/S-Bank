from pydantic import BaseModel as _BaseModel, ConfigDict


class BaseModel(_BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_strip_whitespace=True,
        validate_assignment=True
    )
