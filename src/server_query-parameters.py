from http import HTTPStatus
from datetime import datetime
from fastapi import FastAPI, HTTPException

import logs  # Dummy database

app = FastAPI()


@app.get("/logs")
def logs_query(start: datetime, end: datetime, level: str = None):
    if start >= end:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="start must be before end"
        )
    if not level or not logs.is_valid_level(level):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="invalid log level"
        )

    records = logs.query(start, end, level)
    if not records:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="no logs found")

    return {"count": len(records), "records": records}
