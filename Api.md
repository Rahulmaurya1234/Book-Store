Authentication
--------------
POST   /auth/register
POST   /auth/login
GET    /users/me
PUT    /users/me

Books
-----
GET    /books
GET    /books/{book_id}
POST   /books
PUT    /books/{book_id}
DELETE /books/{book_id}

Authors
-------
GET    /authors
POST   /authors
PUT    /authors/{author_id}
DELETE /authors/{author_id}

Categories
----------
GET    /categories
POST   /categories
PUT    /categories/{category_id}
DELETE /categories/{category_id}

Reviews
-------
POST   /books/{book_id}/reviews
GET    /books/{book_id}/reviews
PUT    /reviews/{review_id}
DELETE /reviews/{review_id}

Orders
------
POST   /orders
GET    /orders
GET    /orders/{order_id}