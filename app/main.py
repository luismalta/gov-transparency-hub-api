from fastapi import FastAPI
from app.routers import revenue, expense


app = FastAPI()

app.include_router(revenue.router)
app.include_router(expense.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}