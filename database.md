# 📚 BookStore Management System - Database Design (V1)

## Business Type

- Online Book Store
- Single Admin Platform
- Customers can register, login, browse books, place orders, and write reviews.
- Admin manages Authors, Categories, Books, and Orders.

---

# Database Tables

## 1. Users

Purpose:
Stores all users of the system.

Fields:

- id (PK)
- full_name
- email (Unique)
- password_hash
- phone
- profile_image
- role (ADMIN / CUSTOMER)
- is_active
- created_at
- updated_at

Relationship:

- One User → Many Orders
- One User → Many Reviews

---

## 2. Authors

Purpose:
Stores all book authors.

Fields:

- id (PK)
- name
- bio
- created_at
- updated_at

Relationship:

- One Author → Many Books

---

## 3. Categories

Purpose:
Stores book categories.

Examples:

- Programming
- AI
- Novel
- Science
- History

Fields:

- id (PK)
- name
- description
- created_at
- updated_at

Relationship:

- One Category → Many Books

---

## 4. Books

Purpose:
Stores all books available in the store.

Fields:

- id (PK)
- title
- description
- isbn
- price
- stock
- language
- published_date
- cover_image
- author_id (FK → Authors.id)
- category_id (FK → Categories.id)
- created_at
- updated_at

Relationship:

- Many Books → One Author
- Many Books → One Category
- One Book → Many Reviews
- One Book → Many Order Items

---

## 5. Reviews

Purpose:
Stores customer reviews.

Fields:

- id (PK)
- rating
- comment
- user_id (FK → Users.id)
- book_id (FK → Books.id)
- created_at

Relationship:

- Many Reviews → One User
- Many Reviews → One Book

Business Rule:

- One user can review multiple books.
- One book can have multiple reviews.

---

## 6. Orders

Purpose:
Stores customer orders.

Fields:

- id (PK)
- user_id (FK → Users.id)
- total_amount
- status
- ordered_at

Status:

- Pending
- Confirmed
- Shipped
- Delivered
- Cancelled

Relationship:

- One User → Many Orders
- One Order → Many Order Items

---

## 7. Order Items

Purpose:
Stores books inside each order.

Fields:

- id (PK)
- order_id (FK → Orders.id)
- book_id (FK → Books.id)
- quantity
- price

Relationship:

- Many Order Items → One Order
- Many Order Items → One Book

Business Rule:

- One Order can contain multiple books.
- One Book can appear in multiple orders.

---

# Relationship Summary

Users
│
├── Orders
│
└── Reviews

Authors
│
└── Books

Categories
│
└── Books

Books
├── Reviews
└── Order Items

Orders
└── Order Items

---

# ER Diagram

                    Users
                      │
          ┌───────────┴────────────┐
          │                        │
          ▼                        ▼
       Orders                  Reviews
          │                        │
          ▼                        │
     Order Items ──────────────────┘
          │
          ▼
        Books
       /     \
      ▼       ▼
 Authors   Categories

---

# Relationships

Users → Orders
One-to-Many

Users → Reviews
One-to-Many

Authors → Books
One-to-Many

Categories → Books
One-to-Many

Books → Reviews
One-to-Many

Orders → Order Items
One-to-Many

Books → Order Items
One-to-Many

---

# Development Order

Phase 1
- Users
- Authentication

Phase 2
- Categories

Phase 3
- Authors

Phase 4
- Books

Phase 5
- Reviews

Phase 6
- Orders

Phase 7
- AWS S3

Phase 8
- Deployment




# USER
-----------
id
full_name
email
password_hash
phone_number
role
is_active
created_at
updated_at

# Role:
    admin
    customer


# 2. Authors
--------------
id (PK)
name
bio
created_at
updated_at


# Relationship:
One Author
      │
      ├── Book 1
      ├── Book 2
      └── Book 3
    

# 3. Categories
-----------------
id (PK)
name
description
created_at
updated_at 

# Examples:
    Programming
    AI
    Novel
    History
    Science


# 4. Books
-----------
id (PK)
title
description
isbn
price
stock
language
published_date
cover_image
author_id (FK)
category_id (FK)
created_at
updated_at


# Relationship
Book
 │
 ├── Author
 │
 └── Category

 Har book:

1 Author
1 Category

# 5. Reviews    
-------------
id (PK)
rating
comment

user_id (FK)

book_id (FK)

created_at

# Relationship
User
   │
   └── Review
          │
          ▼
        Book


# 6. Orders
-----------
orders
---------
id (PK)

user_id (FK)

total_amount

status

ordered_at

# Status
    Pending

    Confirmed

    Delivered

    Cancelled


# Order Items

        Ek order me multiple books ho sakti hain.

        id (PK)

        order_id (FK)

        book_id (FK)

        quantity

        price

Order #25

↓

Python Book

↓

2 Qty

↓

₹600




# Complete Relationship

Users
   │
   ├──────────────┐
   │              │
   ▼              ▼
Orders         Reviews
   │              │
   ▼              │
Order Items ──────┘
      │
      ▼
    Books
   /     \
  ▼       ▼
Author  Category




✅ Primary Key
✅ Foreign Key
✅ One-to-Many Relationships
✅ SQL Joins
✅ CRUD Operations
✅ SQLAlchemy ORM
✅ FastAPI Models
✅ PostgreSQL Design


POST   /auth/register
POST   /auth/login

GET    /books
GET    /books/{id}
POST   /books
PUT    /books/{id}
DELETE /books/{id}

GET    /categories
POST   /categories

GET    /authors
POST   /authors

POST   /reviews

POST   /orders
GET    /orders







              Admin

                │

         Login Dashboard

                │

     ┌──────────┼─────────────┐

     ▼          ▼             ▼

 Add Author  Add Category  Add Book

                               │

                               ▼

                         Customer

                               │

                       Register/Login

                               │

                          Browse Books

                               │

                           Place Order

                               │

                           Add Review







# Book Store me kaun-kaun interact karega?

            
Customer

Admin

Books


#  Business Process
Customer

↓

Register

↓

Login

↓

See Books

↓

Buy Book

↓

Review Book

# Step 3: Admin 

Admin

↓

Add Category

↓

Add Author

↓

Add Book

Phir

Category → categories table

Author → authors table

Book → books table




orders

id = 1

user_id = Rahul

total = 2000



order_items

id = 1
order_id = 1
book_id = Atomic Habits
qty = 1

----------------------

id = 2
order_id = 1
book_id = Python Crash Course
qty = 1

----------------------

id = 3
order_id = 1
book_id = Clean Code
qty = 1