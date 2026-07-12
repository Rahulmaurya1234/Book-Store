# 📚 Project: BookStore Management API

# Final Tech Stack
# Backend
    Python 3.13
    FastAPI
    Uvicorn
# Database
    PostgreSQL
    SQLAlchemy 2.0
    Alembic
# Authentication
    JWT
    Passlib (Password Hashing)
# Storage
    AWS S3
# Deployment
    Docker
    EC2
    Nginx

# Testing
        Postman
        Pytest




# Software Architecture

                 Client

       React / Mobile / Postman

                │
                ▼

          FastAPI Backend

        Router (Endpoints)

                │

          Business Logic

             Services

                │

           SQLAlchemy ORM

                │

           PostgreSQL DB

                │

         AWS S3 (Images)



# Phase 1
#   Requirement Analysis

# Functional Requirements

# Authentication
    Register
    Login
    Logout
    Refresh Token

# Users
    Update Profile
    Change Password
    Upload Avatar

# Books
    Add Book
    Update Book
    Delete Book
    Get Single Book
    Get All Books
    Search Book
    Pagination

# Categories
    Create
    Update
    Delete

# Authors
    CRUD

# Reviews
    Add Review
    Update Review
    Delete Review
    Average Rating

# Orders   
    Buy Book
    Order History
    Order Items


# Admin
    Manage Users
    Manage Books
    Manage Categories
    Dashboard

#   AWS
    Upload Book Image to S3
    Upload Profile Image
    Deploy on EC2



# Non Functional Requirements




✅ Secure

✅ Fast

✅ Scalable

✅ Modular

✅ Clean Code

✅ Logging

✅ Exception Handling

✅ Validation


# Architecture Diagram



                  Client (React/Postman)

                         │
                     HTTP Request

                         │

                    FastAPI Backend

      ┌───────────────┬───────────────┐
      │               │               │
   Routers        Services      Middleware
      │               │
      └───────────────┘
              │
         Repository Layer
              │
         SQLAlchemy ORM
              │
        PostgreSQL Database
              │
         AWS S3 (Images)



#   folder structure 

bookstore-api/

│

├── app/

│   ├── api/

│   │     ├── v1/

│   │     │      ├── auth.py

│   │     │      ├── users.py

│   │     │      ├── books.py

│   │     │      ├── categories.py

│   │     │      ├── reviews.py

│   │     │      └── orders.py

│   │

│   ├── core/

│   │      ├── config.py

│   │      ├── security.py

│   │      └── database.py

│   │

│   ├── models/

│   ├── schemas/

│   ├── repositories/

│   ├── services/

│   ├── utils/

│   ├── middleware/

│   ├── exceptions/

│   └── main.py

│

├── tests/

├── alembic/

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .env

└── README.md



# Database Design

users

books

categories

authors

orders

order_items

reviews

wishlist

# relationships

User
│
├── Orders
├── Reviews
└── Wishlist

Book
│
├── Category
├── Author
├── Reviews
└── Order Items


# Phase 3

bookstore-api/

app/

core/

api/

models/

schemas/

services/

repositories/

utils/

middlewares/

exceptions/

database/

tests/

Dockerfile

docker-compose.yml

README.md




# API Endpoints

POST   /auth/register

POST   /auth/login

GET    /books

POST   /books

PUT    /books/{id}

DELETE /books/{id}

GET    /orders

POST   /orders




ER Diagram banayenge
Relationships samjhenge
Primary Key
Foreign Key
One-to-One
One-to-Many
Many-to-Many
Normalization



bookstore-api/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── books.py
│   │       ├── authors.py
│   │       ├── categories.py
│   │       ├── reviews.py
│   │       └── orders.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   ├── repositories/
│   │
│   ├── services/
│   │
│   ├── utils/
│   │
│   └── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md


| Folder       | Purpose                    |
| ------------ | -------------------------- |
| api          | Endpoints (Routes)         |
| core         | Database, Config, Security |
| models       | SQLAlchemy Models          |
| schemas      | Pydantic Models            |
| repositories | Database Queries           |
| services     | Business Logic             |
| utils        | Helper Functions           |
| main.py      | FastAPI App Start          |
