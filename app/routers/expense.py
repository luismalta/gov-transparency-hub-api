from fastapi import APIRouter

router = APIRouter(
    prefix="/expense",
    tags=["expense"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_expense():
    return {"Hello": "expense"}