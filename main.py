from fastapi import FastAPI, Form, Request, Depends
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import schema, models
from database import SessionLocal, engine
from schema import region
from models import region

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='enlabolsa Dashboard')
templates = Jinja2Templates (directory="templates")

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app.mount("/index", StaticFiles(directory="templates"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def guardar_region(request: Request, db: Session = Depends(get_database_session)):
    records = db.query(region).all()
    return templates.TemplateResponse("index.html", {"request": request, "data": records})

@app.get("/region", response_class=HTMLResponse)
def mostrar_region(request: Request, name: schema.region.nombre_region, db: Session = Depends(get_database_session)):
    item = db.query(region).filter(region.id==name).first()
    print(item)
    return templates.TemplateResponse("index.html", {"request": request, "region": item})

@app.post("/region")
async def crear_region(db: Session = Depends(get_database_session), nombre_region: schema.region.nombre_region = Form(...)):
    region = region(nombre_region=nombre_region)
    db.add(region)
    db.commit()
    response = RedirectResponse('/', status_code=303)
    return response





if __name__ == "__main__":
    uvicorn.run("fastapi_code:app")
