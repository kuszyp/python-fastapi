import asyncio
from time import sleep
from fastapi import FastAPI

app = FastAPI()


# hey -c 10 -n 10 http://localhost:8000/sleep/sys
@app.get("/sleep/sys")
def nsys_sleep():
    sleep(1)
    return {"error": None}


# hey -c 10 -n 10 http://localhost:8000/sleep/async-sys
@app.get("/sleep/async-sys")
async def sys_sleep():
    sleep(1)
    return {"error": None}


# hey -c 10 -n 10 http://localhost:8000/sleep/async-aio
@app.get("/sleep/async-aio")
async def aio_sleep():
    await asyncio.sleep(1)
    return {"error": None}
