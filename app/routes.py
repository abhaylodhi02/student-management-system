from fastapi import APIRouter, HTTPException
from app.models import Student
from app.db import student_collection
from bson import ObjectId
from bson.errors import InvalidId

student_routes = APIRouter()

# Helper function to serialize ObjectId to string
def serialize_objectid(value: dict) -> dict:
    """
    Recursively converts ObjectId fields to strings in a dictionary.
    """
    if isinstance(value, dict):
        return {k: serialize_objectid(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [serialize_objectid(item) for item in value]
    elif isinstance(value, ObjectId):
        return str(value)
    return value

# Create a student
@student_routes.post("/", status_code=201)
async def create_student(student: Student):
    result = await student_collection.insert_one(student.dict())
    return {"id": str(result.inserted_id)}

# List students
@student_routes.get("/")
async def list_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age is not None:
        query["age"] = {"$gte": age}
    
    students = await student_collection.find(query).to_list(100)

    # Serialize ObjectId to string in the list of students
    return {"data": [serialize_objectid(student) for student in students]}

# Fetch student by ID
@student_routes.get("/{id}")
async def fetch_student(id: str):
    try:
        student = await student_collection.find_one({"_id": ObjectId(id)})
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        
        # Serialize ObjectId to string and remove the original _id field
        student["id"] = str(student["_id"])
        del student["_id"]
        
        return serialize_objectid(student)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID")

# Update student by ID
@student_routes.patch("/{id}", status_code=204)
async def update_student(id: str, student: Student):
    try:
        update_data = {k: v for k, v in student.dict().items() if v is not None}
        result = await student_collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID")

# Delete student by ID
@student_routes.delete("/{id}", status_code=200)
async def delete_student(id: str):
    try:
        result = await student_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID")
