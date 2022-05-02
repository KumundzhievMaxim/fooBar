from typing import Dict
from pydantic import BaseModel


class Response(BaseModel):
    search_interest: Dict
