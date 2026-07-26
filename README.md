# \# Restaurant Order API
#
# \## Overview
# 
# This project is a REST API developed as part of the Python Developer Technical Assessment.
# 
# The API is built using \*\*Python\*\*, \*\*FastAPI\*\*, \*\*SQLAlchemy\*\*, and \*\*SQLite\*\*. It provides a list of restaurant orders along with complete order details, menu information, and payment details.
# 
# \---
# 
# \## Tech Stack
# 
# \- Python 3.x
# \- FastAPI
# \- SQLAlchemy
# \- SQLite
# \- Uvicorn
# \- Postman
# \- Swagger UI
# 
# \---
# 
# \## Project Structure
# 
# ```
# Restaurant\_API\_Project/
# │
# ├── app.py
# ├── database.py
# ├── models.py
# ├── schemas.py
# ├── create\_db.py
# ├── restaurant.db
# ├── requirements.txt
# ├── routers/
# │   └── orders.py
# └── README.md
# ```
# 
# \---
# 
# \## Database Tables
# 
# The project uses three tables:
# 
# \### Menu
# Stores menu item information.
# 
# \- Item ID
# \- Item Name
# \- Category ID
# \- Menu ID
# \- Available Sizes
# \- Price
# 
# \### Order History
# 
# Stores all ordered items.
# 
# \- Order ID
# \- Item ID
# \- Size
# \- Price
# \- Quantity
# \- Order Status
# \- Total
# 
# \### Payments
# 
# Stores payment details for each order.
# 
# \- Payment ID
# \- Order ID
# \- Amount Due
# \- Tips
# \- Discount
# \- Total Paid
# \- Payment Type
# \- Payment Status
# 
# \---
# 
# \## API Endpoint
# 
# \### Get All Orders
# 
# \*\*Method\*\*
# 
# ```
# GET /orders/
# ```
# 
# Returns:
# 
# \- Order Details
# \- Ordered Items
# \- Menu Information
# \- Payment Information
# 
# \---
# 
# \## Installation
# 
# Clone the project or extract the ZIP file.
# 
# Install dependencies:
# 
# ```bash
# pip install -r requirements.txt
# ```
# 
# \---
# 
# \## Run the Application
# 
# Start the FastAPI server:
# 
# ```bash
# uvicorn app:app --reload
# ```
# 
# Server runs at:
# 
# ```
# http://127.0.0.1:8000
# ```
# 
# \---
# 
# \## Swagger Documentation
# 
# Open:
# 
# ```
# http://127.0.0.1:8000/docs
# ```
# 
# Swagger UI can be used to test the API.
# 
# \---
# 
# \## Postman Testing
# 
# Request:
# 
# ```
# GET http://127.0.0.1:8000/orders/
# ```
# 
# Expected Response:
# 
# \- HTTP Status: \*\*200 OK\*\*
# \- JSON containing order details, menu information, and payment details.
# 
# \---
# 
# \## Features
# 
# \- FastAPI REST API
# \- SQLite Database
# \- SQLAlchemy ORM
# \- Order and Payment Integration
# \- Menu Data Integration
# \- Nested JSON Response
# \- Swagger Documentation
# \- Postman Tested
# 
# \---
# 
# \## Database Relationships
# 
# \- \*\*Menu\*\* is linked with \*\*Order History\*\* using `item\_id`.
# \- \*\*Order History\*\* is linked with \*\*Payments\*\* using `order\_id`.
# 
# \---
# 
# \## Future Improvements
# 
# \- Authentication using JWT
# \- Pagination
# \- Search and Filtering
# \- Better Exception Handling
# \- Logging
# \- MySQL Support
# \- Docker Deployment
# 
# \---
# 
# \## Author
# 
# \*\*Gangam Ayyappa Asrith\*\*
# 
# Python Developer Assessment Submission

