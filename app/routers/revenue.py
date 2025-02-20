from fastapi import APIRouter
from datetime import datetime
from app.dtos.revenue_dto import RevenueResponseDto
from app.repositories.revenue import get_revenue


router = APIRouter(
    prefix="/revenue",
    tags=["revenue"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_expense_by_date(
    municipio: str,
    data: datetime = None,
    codigo_receita: str = None,
    fonte_recurso: str = None
) -> list[RevenueResponseDto]:
    data =  {
        "municipio": municipio,
        "data": data,
        "codigo_receita": codigo_receita,
        "fonte_recurso": fonte_recurso
    }
    return get_revenue(data)