from fastapi import APIRouter, Query
from typing import Annotated
from app.dtos.revenue_dto import RevenueResponseDto, RevenueFilterParams
from app.repositories.revenue import get_revenue


router = APIRouter(
    prefix="/revenue",
    tags=["revenue"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def download_revenue(filter_query: Annotated[RevenueFilterParams, Query()]) -> list[RevenueResponseDto]:
    return get_revenue(filter_query.model_dump(mode='python'))