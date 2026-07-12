# 📚 Book Management System API

A production-style REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy** using a layered architecture (Router → Service → Repository). The project provides JWT authentication, role-based authorization, book management, shopping cart, order management, and review functionality.

---

## 🚀 Features

### 🔐 Authentication
- User Registration
- User Login
- JWT Authentication
- Password Hashing (bcrypt)
- Protected Routes
- Role-Based Access Control (Admin / Customer)

### 👤 Users
- Register User
- Login User
- Get Current User Profile (`/users/me`)

### ✍️ Authors
- Create Author (Admin)
- Update Author (Admin)
- Delete Author (Admin)
- Get All Authors
- Get Author By ID

### 📂 Categories
- Create Category (Admin)
- Update Category (Admin)
- Delete Category (Admin)
- Get All Categories
- Get Category By ID

### 📚 Books
- Create Book (Admin)
- Update Book (Admin)
- Delete Book (Admin)
- Get All Books
- Get Book By ID

### 🛒 Shopping Cart
- Get Cart
- Add Book to Cart
- Update Cart Item Quantity
- Remove Cart Item
- Clear Cart

### 📦 Orders
- Checkout
- Create Order
- Create Order Items
- Reduce Book Stock

### ⭐ Reviews
- Add Review
- Update Review
- Delete Review
- Get Book Reviews

---

# 🏗️ Architecture

```
Client
   │
   ▼
FastAPI Router
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

---

# 📁 Project Structure

```
Book_management/
│
├── alembic/
├── app/
│   ├── api/
│   ├── core/
│   ├── dependencies/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── main.py
│
├── requirements.txt
├── alembic.ini
├── .env.example
└── README.md
```

---

# 🛠 Tech Stack

- FastAPI
- Python 3.13
- PostgreSQL
- SQLAlchemy ORM
- Alembic
- Pydantic v2
- JWT Authentication
- Passlib (bcrypt)
- Uvicorn

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Book_management.git

cd Book_management
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bookstore_db
DB_USER=postgres
DB_PASSWORD=your_password

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Run Database Migration

```bash
alembic upgrade head
```

---

## Start Server

```bash
uvicorn app.main:app --reload
```

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🔑 Authentication

1. Register User

```
POST /auth/register
```

2. Login

```
POST /auth/login
```

3. Copy JWT Token

4. Click **Authorize** in Swagger

5. Enter

```
Bearer YOUR_ACCESS_TOKEN
```

---

# Database Schema

```
Users
│
├── Orders
│      │
│      └── OrderItems
│
├── Reviews
│
└── Cart
       │
       └── CartItems

Authors
│
└── Books
       │
Categories
       │
       └── Books
```

---

# Security

- JWT Authentication
- Password Hashing
- Role-Based Authorization
- Protected Endpoints
- Admin Only Routes

---

# Future Improvements

- Pagination
- Search
- Filtering
- Sorting
- AWS S3 Image Upload
- AWS Secrets Manager
- Docker
- Nginx
- EC2 Deployment
- CI/CD Pipeline

---

# Author

**Rahul Maurya**

Backend Developer | Python | FastAPI | PostgreSQL | AWS

GitHub:
https://github.com/YOUR_USERNAME