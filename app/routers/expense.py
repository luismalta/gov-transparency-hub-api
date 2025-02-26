from fastapi import APIRouter
from app.dtos.expense_dto import ExpenseDetailsResponseDto, ExpenseItemResponseDto, ExpenseInvoiceResponseDto
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
    municipio: str,
) -> list[ExpenseDetailsResponseDto]:
    data =  {
        "municipio": municipio,
    }
    return get_expense_details(data)


@router.get("/itens")
def download_expense_itens(
    municipio: str,
) -> list[ExpenseItemResponseDto]:
    data =  {
        "municipio": municipio,
    }
    return get_expense_itens(data)

@router.get("/invoices")
def download_expense_invoices(
    municipio: str,
) -> list[ExpenseInvoiceResponseDto]:
    data =  {
        "municipio": municipio,
    }
    return get_expense_invoices(data)