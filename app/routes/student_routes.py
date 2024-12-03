from fastapi import APIRouter, HTTPException, Path, Query
from app.models import Student, UpdateStudent
from config.db import get_database

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/", status_code=201)
async def create_student(student: Student):
    db = await get_database()
    result = await db.students.insert_one(student.dict())
    return {"id": str(result.inserted_id)}

@router.get("/")
async def list_students(country: str = Query(None), age: int = Query(None)):
    db = await get_database()
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = await db.students.find(query).to_list(100)
    return {"data": students}
