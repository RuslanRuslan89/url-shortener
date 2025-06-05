from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import redis
import secrets

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def generate_short_code() -> str:
    return secrets.token_urlsafe(4)  # Например, "xYz1"

@app.post("/shorten")
async def shorten_url(url: str):
    short_code = generate_short_code()
    redis_client.set(short_code, url)
    return {"short_url": f"http://localhost:8000/{short_code}"}

@app.get("/{short_code}")
async def redirect(short_code: str):
    original_url = redis_client.get(short_code)
    if not original_url:
        raise HTTPException(status_code=404)
    return RedirectResponse(original_url.decode())
