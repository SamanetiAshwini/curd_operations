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

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
