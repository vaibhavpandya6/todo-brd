```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.utils import generate_short_code, validate_url
from app.database import save_url, get_url_by_short_code, increment_click_count

app = FastAPI()

class URLRequest(BaseModel):
    original_url: str

class URLResponse(BaseModel):
    short_url: str

@app.post("/shorten", response_model=URLResponse)
async def shorten_url(url_request: URLRequest):
    original_url = url_request.original_url
    if not validate_url(original_url):
        raise HTTPException(status_code=400, detail="Invalid URL")

    short_code = generate_short_code()
    save_url(original_url, short_code)
    return {"short_url": f"http://localhost/{short_code}"}

@app.get("/redirect/{short_code}")
async def redirect(short_code: str):
    try:
        url = get_url_by_short_code(short_code)
        if not url:
            raise HTTPException(status_code=404, detail="URL not found")

        increment_click_count(short_code)
        return {"url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history():
    # Implement history API
    pass