from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class Student(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    course: str = Field(min_length=1)
    age: int

students = []

next_id = 1

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):

    global next_id

    for existing_student in students:
        if existing_student["email"] == student.email:
            raise HTTPException(
                status_code=400,
                detail="Student already exists"
            )

    new_student = {
        "id": next_id,
        "name": student.name,
        "email": student.email,
        "course": student.course,
        "age": student.age
    }

    students.append(new_student)

    next_id += 1

    return new_student

@app.get("/students")
def get_students():

    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    for existing_student in students:

        if existing_student["id"] == student_id:

            for other_student in students:

                if (
                    other_student["email"] == student.email
                    and other_student["id"] != student_id
                ):
                    raise HTTPException(
                        status_code=400,
                        detail="Email already exists"
                    )

            # Update student
            existing_student["name"] = student.name
            existing_student["email"] = student.email
            existing_student["course"] = student.course
            existing_student["age"] = student.age

            return existing_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

@app.get("/students/search")
def search_students(course: str):

    results = []

    for student in students:

        if course.lower() in student["course"].lower():
            results.append(student)

    return results