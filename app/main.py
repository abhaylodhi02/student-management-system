from fastapi import FastAPI
from app.routes import student_routes
from config.db import connect_to_db

app = FastAPI(
    title="Student Management System",
    version="1.0.0",
    description="Backend for managing students using FastAPI and MongoDB Atlas."
)

@app.on_event("startup")
async def startup_event():
    await connect_to_db()

# Include student routes
app.include_router(student_routes.router)
