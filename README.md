# 🚀 FastAPI & MongoDB Async Boilerplate

A professional-grade starter template for building scalable, asynchronous REST APIs using **FastAPI** and **MongoDB**. 

---

## 🛠 Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **FastAPI** | High-performance Python web framework |
| **Motor** | Non-blocking MongoDB driver for asyncio |
| **Pydantic** | Data validation and settings management |
| **Uvicorn** | Lightning-fast ASGI server implementation |
| **Python-Dotenv** | Secure environment variable handling |

---

## ✨ Key Features

* **Full CRUD Integration** – Pre-configured Create, Read, Update, and Delete operations.
* **Asynchronous Architecture** – Fully non-blocking database I/O using `Motor`.
* **Robust Validation** – Strict schema enforcement using Pydantic models.
* **Scalable Structure** – Organized folder structure separating routes and business logic.

---


## ⚙️ Getting Started

### 1. Clone & Navigate
git clone git@github.com:RimDH/fastApi-demo.git

cd fastApi-demo

### 2. Environment Setup
Create a virtual environment and install dependencies:

## Create the environment
python3 -m venv venv

## Activate it (Linux/macOS)
source venv/bin/activate  

## Activate it (Windows)
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

### 3. Configuration
Create a .env file in the root directory and add your credentials:

MONGO_URI=mongodb://localhost:27017

DB_NAME=fastapi_demo

---

## 🚀 Running the Application

### Development
Launch the server with Hot-Reload enabled:

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

* API Base URL: http://localhost:8000


