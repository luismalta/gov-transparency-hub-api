import os
from fastapi import FastAPI
from app.routers import revenue, expense
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(revenue.router)
app.include_router(expense.router)

script_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(script_dir, "static")

app.mount("/", StaticFiles(directory=static_dir,html = True), name="static")  
