from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from config import Config
{{ db_import }}
{{ auth_import }}

app = FastAPI(title="{{ project_name }}", version="1.0.0")

{{ db_init }}

class Item(BaseModel):
    name: str
    description: str | None = None

@app.get("/", response_class=HTMLResponse)
async def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ project_name }} - Home</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <h1>Bem-vindo ao {{ project_name }}!</h1>
        <p>Projeto FastAPI gerado com sucesso.</p>
        <script src="/static/js/main.js"></script>
    </body>
    </html>
    '''

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item {item.name} criado com sucesso!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=Config.PORT)