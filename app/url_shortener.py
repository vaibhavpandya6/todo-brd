import secrets
import string
from typing import Optional

from app import database

def generate_short_code(original_url: str) -> str:
    short_code = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))
    database.create_shortened_url(original_url, short_code)
    return short_code

def get_original_url(short_code: str) -> Optional[str]:
    return database.get_original_url(short_code)