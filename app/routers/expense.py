from fastapi import APIRouter, Query
from typing import Annotated
from app.dtos.expense_dto import ExpenseDetailsResponseDto, ExpenseItemResponseDto, ExpenseInvoiceResponseDto, ExpenseDetailsFilterParams, ExpenseItemFilterParams, ExpenseInvoiceFilterParams
from app.repositories.expense_details import get_expense_details
from app.repositories.expense_itens import get_expense_itens
from app.repositories.expense_invoices import get_expense_invoices
from . import _extract_pagination

router = APIRouter(
    prefix="/expense",
    tags=["expense"],
    responses={404: {"description": "Not found"}},
)


@router.get("/details")
def download_expense_details(
    filter_query: Annotated[ExpenseDetailsFilterParams, Query()]
) -> list[ExpenseDetailsResponseDto]:
    pagination_info, filters = _extract_pagination(filter_query.model_dump(mode='python'))
    parsed_filters = {k: v for k, v in filters.items() if v is not None}
    return get_expense_details(parsed_filters, pagination_info)


@router.get("/itens")
def download_expense_itens(
    filter_query: Annotated[ExpenseItemFilterParams, Query()]
) -> list[ExpenseItemResponseDto]:
    pagination_info, filters = _extract_pagination(filter_query.model_dump(mode='python'))
    parsed_filters = {k: v for k, v in filters.items() if v is not None}
    return get_expense_itens(parsed_filters, pagination_info)

@router.get("/invoices")
def download_expense_invoices(
    filter_query: Annotated[ExpenseInvoiceFilterParams, Query()]
) -> list[ExpenseInvoiceResponseDto]:
    pagination_info, filters = _extract_pagination(filter_query.model_dump(mode='python'))
    parsed_filters = {k: v for k, v in filters.items() if v is not None}
    return get_expense_invoices(parsed_filters, pagination_info)