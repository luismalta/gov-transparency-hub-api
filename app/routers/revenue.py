from fastapi import APIRouter, Query
from typing import Annotated
from app.dtos.revenue_dto import RevenueResponseDto, RevenueFilterParams
from app.repositories.revenue import get_revenue
from . import _extract_pagination


router = APIRouter(
    prefix="/revenue",
    tags=["revenue"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def download_revenue(filter_query: Annotated[RevenueFilterParams, Query()]) -> list[RevenueResponseDto]:
    pagination_info, filters = _extract_pagination(filter_query.model_dump(mode='python'))
    parsed_filters = {k: v for k, v in filters.items() if v is not None}
    return get_revenue(parsed_filters, pagination_info)