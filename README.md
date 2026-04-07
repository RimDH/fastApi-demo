- Create, Read, Update, Delete (CRUD) operations for users  
- Async MongoDB integration with **Motor**  
- Environment variable support using **python-dotenv**  
- Input validation with **Pydantic**  
- Clean project structure for scalability  

---

## Tech Stack

- **FastAPI** – Web framework  
- **Uvicorn** – ASGI server  
- **MongoDB + Motor** – Async database  
- **Pydantic + Pydantic-Settings** – Data validation and settings  
- **Python-Dotenv** – Environment variables  

---

## Project Structure


fastapi-demo/
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── routes/ # API routes
│ ├── controllers/ # Business logic
│ ├── schemas/ # Pydantic models
│ ├── db.py # Database connection
│ └── core/
│ └── config.py # Environment settings
├── venv/ # Python virtual environment (not in git)
├── .env # Environment variables
├── requirements.txt # Python dependencies
└── README.md


---

## Setup

### 1. Clone the project

```bash
git clone <repo-url>
cd fastapi-demo
2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Set up environment variables

Create .env file:

MONGO_URI=mongodb://localhost:27017
DB_NAME=fastapi_demo
Running the App
Development
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
--reload → auto-reload on code changes
API available at: http://127.0.0.1:8000