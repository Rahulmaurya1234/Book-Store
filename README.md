Book
   │
   ├── Author
   └── Category

Order
   └── User

Review
   ├── User
   └── Book


Authors
   │
   │
   ▼
Books
   │
   ├──────────┐
   ▼          ▼
Reviews    OrderItems
   ▲          ▲
   │          │
Users      Orders
   │          ▲
   └──────────┘# Book-Store
