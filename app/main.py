from fastapi import FastAPI
from fastapi.requests import Request
from datetime import datetime

app = FastAPI()


@app.get("/endpoint")
async def endpint1(request: Request):
    return {"url": str(request.url), "now": datetime.utcnow()}
