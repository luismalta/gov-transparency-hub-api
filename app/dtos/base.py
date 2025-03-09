from pydantic import BaseModel, Field
from . import constants


class BaseFilterParams(BaseModel):
    page: int = Field(0, ge=0, description=constants.PAGE)
    page_size: int = Field(100, ge=1, le=100, description=constants.PAGE_SIZE)
