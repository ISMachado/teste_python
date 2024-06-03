from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Data
from schemas import DataResponse
from datetime import datetime

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/data/", response_model=List[DataResponse])
def read_data(start: datetime, end: datetime, db: Session = Depends(get_db)):
    return db.query(Data).filter(Data.timestamp.between(start, end)).all()
