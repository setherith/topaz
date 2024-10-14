from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def index():
    return {
        "Project": "Topaz",
        "Module": "API",
        "Version": "v0.1",
        "Description": "Database connection service"
        }

@app.get('/children')
async def list_children():
    return ['Child1', 'Child2', 'Child3']