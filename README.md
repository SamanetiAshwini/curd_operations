# Student Management API (CRUD Operations)

A fast, lightweight RESTful API built with **FastAPI** and **Pydantic** for managing student records. This project demonstrates core CRUD (Create, Read, Update, Delete) operations and search functionality with data validation.

---

## 🚀 Features

- **Create Student (`POST`)**: Register a new student with unique email validation.
- **Get All Students (`GET`)**: Retrieve the complete list of students.
- **Get Student by ID (`GET`)**: Retrieve a specific student by their unique ID.
- **Search Students (`GET`)**: Filter students by course name.
- **Update Student (`PUT`)**: Modify student details while maintaining email uniqueness.
- **Delete Student (`DELETE`)**: Remove a student record by ID.
- **Data Validation**: Automatic request schema validation using Pydantic models.
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern web framework for building APIs with Python.
- **[Uvicorn](https://www.uvicorn.org/)**: Lightning-fast ASGI server.
- **[Pydantic](https://docs.pydantic.dev/)**: Data validation and settings management using Python type annotations.

---

## 📦 Project Structure

```text
curd_operations/
├── main.py          # FastAPI application & route endpoints
├── README.md        # Project documentation
└── .gitignore       # Git ignored files
```

---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone git@github.com:SamanetiAshwini/curd_operations.git
cd curd_operations
```

### 2. Create and Activate Virtual Environment (Optional but recommended)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn pydantic[email]
```

### 4. Run the Server
```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

---

## 📖 API Documentation & Interactive Docs

Once the server is running, visit:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔌 API Endpoints

### 1. Student Schema

| Field | Type | Description | Validation |
| :--- | :--- | :--- | :--- |
| `name` | `string` | Full name of the student | Minimum length: 1 |
| `email` | `string` | Email address | Valid email format, unique |
| `course` | `string` | Enrolled course | Minimum length: 1 |
| `age` | `integer` | Age of student | Integer |

---

### 2. Endpoints Summary

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `POST` | `/students` | Create a new student | `201 Created` |
| `GET` | `/students` | Get all students | `200 OK` |
| `GET` | `/students/{student_id}` | Get student by ID | `200 OK` / `404 Not Found` |
| `GET` | `/students/search?course={name}` | Search students by course | `200 OK` |
| `PUT` | `/students/{student_id}` | Update student details | `200 OK` / `404 Not Found` |
| `DELETE` | `/students/{student_id}` | Delete student by ID | `200 OK` / `404 Not Found` |

---

### 3. Example Requests & Responses

#### **Create Student**
- **`POST /students`**
- **Request Body**:
  ```json
  {
    "name": "Ashwini Samaneti",
    "email": "ashwini@example.com",
    "course": "Computer Science",
    "age": 22
  }
  ```
- **Response (`201 Created`)**:
  ```json
  {
    "id": 1,
    "name": "Ashwini Samaneti",
    "email": "ashwini@example.com",
    "course": "Computer Science",
    "age": 22
  }
  ```

#### **Get All Students**
- **`GET /students`**
- **Response (`200 OK`)**:
  ```json
  [
    {
      "id": 1,
      "name": "Ashwini Samaneti",
      "email": "ashwini@example.com",
      "course": "Computer Science",
      "age": 22
    }
  ]
  ```

#### **Delete Student**
- **`DELETE /students/1`**
- **Response (`200 OK`)**:
  ```json
  {
    "message": "Student deleted successfully"
  }
  ```

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
