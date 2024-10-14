from fastapi import FastAPI

app = FastAPI()

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
    return ['ChildA', 'ChildB']