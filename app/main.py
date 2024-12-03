from fastapi import FastAPI
from app.routes import student_routes
from fastapi.responses import FileResponse

app = FastAPI(
    title="Student Management System",
    description="API Layer for managing students using FastAPI and MongoDB.",
    version="1.0.0"
)

# Root URL Route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student Management System"}

# Include the student routes
app.include_router(student_routes, prefix="/students", tags=["Students"])

# Favicon Route (Optional)
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("path_to_your_favicon/favicon.ico")  # Replace with actual path if available
