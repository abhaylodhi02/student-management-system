# student-management-system
Backend for Student Management System using FastAPI and MongoDB Atlas.


# For Testing

Base URL
https://student-management-system-uvmo.onrender.com
Endpoints
Create a Student

URL: /
Method: POST
Description: Adds a new student to the database.
Request Body:
{
  "name": "John Doe",
  "age": 20,
  "address": {
    "country": "India",
    "city": "New Delhi"
  }
}
Response:
{
  "id": "64c7f06e9343e9abc7f49d81"
}
List Students

URL: /
Method: GET
Description: Fetches a list of students, optionally filtered by country or age.
Query Parameters:
country (optional): Filters students by their country.
age (optional): Filters students with age greater than or equal to the provided value.
Example Request:
GET /?country=India&age=18
Response:
{
  "data": [
    {
      "id": "64c7f06e9343e9abc7f49d81",
      "name": "John Doe",
      "age": 20,
      "address": {
        "country": "India",
        "city": "New Delhi"
      }
    }
  ]
}
Fetch a Student by ID

URL: /{id}
Method: GET
Description: Fetches a student by their unique ID.
Path Parameter:
id: The unique identifier of the student.
Example Request:
GET /64c7f06e9343e9abc7f49d81
Response:
{
  "id": "64c7f06e9343e9abc7f49d81",
  "name": "John Doe",
  "age": 20,
  "address": {
    "country": "India",
    "city": "New Delhi"
  }
}
Update a Student by ID

URL: /{id}
Method: PATCH
Description: Updates the details of a student by their unique ID.
Path Parameter:
id: The unique identifier of the student.
Request Body: (Only include fields you want to update.)
{
  "name": "Jane Doe",
  "age": 22
}
Response:
No content (status 204 if successful).
Delete a Student by ID

URL: /{id}
Method: DELETE
Description: Deletes a student by their unique ID.
Path Parameter:
id: The unique identifier of the student.
Example Request:
DELETE /64c7f06e9343e9abc7f49d81
Response:
{
  "message": "Student deleted successfully"
}
Notes:
Replace {id} in the URLs with the actual student ID.
Ensure the student_collection in your database contains the expected data structure for students.
