import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the MONGO_URI from the environment variables
mongo_uri = os.getenv("MONGODB_URI")

# Check if the MONGO_URI is loaded correctly
if not mongo_uri:
    raise ValueError("MONGODB_URI environment variable not found. Please set it in the .env file.")

# Establish connection to MongoDB Atlas
try:
    client = AsyncIOMotorClient(mongo_uri)
    database = client.get_database("student_management")
    student_collection = database.get_collection("students")
    print("Connected to MongoDB Atlas!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
