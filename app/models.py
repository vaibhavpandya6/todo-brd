from pydantic import BaseModel
from datetime import datetime

class URL(BaseModel):
    id: int
    original_url: str
    short_code: str
    date_created: datetime
    click_count: int