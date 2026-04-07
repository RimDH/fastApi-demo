# FastAPI CRUD Demo

A simple CRUD application using **FastAPI** and **MongoDB**, following clean code and maintainable structure.

---

## Features

- Create, Read, Update, Delete (CRUD) operations for users
- Async MongoDB integration with **Motor**
- Environment variable support using **python-dotenv**
- Input validation with **Pydantic**
- Clean code for scalability and maintainability

---

## Tech Stack

- **FastAPI** – Web framework
- **Uvicorn** – ASGI server
- **MongoDB + Motor** – Async database
- **Pydantic + Pydantic-Settings** – Data validation and settings
- **Python-Dotenv** – Environment variables

---

## Setup

1. **Clone the project**

```bash
git clone <repo-url>
cd fastapi-demo
Create a virtual environment
python3 -m venv venv
source venv/bin/activate
Install dependencies
pip install -r requirements.txt
Set up environment variables

Create a .env file:

MONGO_URI=mongodb://localhost:27017
DB_NAME=fastapi_demo