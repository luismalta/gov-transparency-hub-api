from fastapi import APIRouter, Query
from typing import Annotated
from app.dtos.expense_dto import ExpenseDetailsResponseDto, ExpenseItemResponseDto, ExpenseInvoiceResponseDto, ExpenseDetailsFilterParams, ExpenseItemFilterParams, ExpenseInvoiceFilterParams
from app.repositories.expense_details import get_expense_details
from app.repositories.expense_itens import get_expense_itens
from app.repositories.expense_invoices import get_expense_invoices

router = APIRouter(
    prefix="/expense",
    tags=["expense"],
    responses={404: {"description": "Not found"}},
)


@router.get("/details")
def download_expense_details(
    filter_query: Annotated[ExpenseDetailsFilterParams, Query()]
) -> list[ExpenseDetailsResponseDto]:
    return get_expense_details(filter_query.model_dump(mode='python'))


@router.get("/itens")
def download_expense_itens(
    filter_query: Annotated[ExpenseItemFilterParams, Query()]
) -> list[ExpenseItemResponseDto]:
    return get_expense_itens(filter_query.model_dump(mode='python'))

@router.get("/invoices")
def download_expense_invoices(
    filter_query: Annotated[ExpenseInvoiceFilterParams, Query()]
) -> list[ExpenseInvoiceResponseDto]:
    return get_expense_invoices(filter_query.model_dump(mode='python'))