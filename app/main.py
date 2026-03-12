from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from typing import Optional
from pydantic import BaseModel

from app import url_shortener
from app import database

app = FastAPI()

class UrlRequest(BaseModel):
    original_url: str

@app.post("/shorten")
async def shorten_url(request: UrlRequest):
    try:
        short_code = url_shortener.generate_short_code(request.original_url)
        return {"short_url": f"http://localhost/{short_code}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/{short_code}")
async def redirect_to_original(short_code: str):
    try:
        original_url = url_shortener.get_original_url(short_code)
        return RedirectResponse(original_url, status_code=301)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/")
async def display_link_history():
    try:
        link_history = database.get_all_shortened_urls()
        return {"link_history": link_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))