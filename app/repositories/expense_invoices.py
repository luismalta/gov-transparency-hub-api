from datetime import datetime
from app.db.db_models import ExpenseInvoiceDBModel
from app.db.db_connection import Session

from app.dtos.expense_dto import ExpenseInvoiceResponseDto

def _db_to_dto(expense_detail: ExpenseInvoiceDBModel) -> ExpenseInvoiceResponseDto:
    return ExpenseInvoiceResponseDto(
        codigo=expense_detail.codigo,
        tipo=expense_detail.tipo,
        numero_despesa=expense_detail.numero_despesa,
        ano_despesa=expense_detail.ano_despesa,
        nota_fiscal=expense_detail.nota_fiscal,
        serie=expense_detail.serie,
        data_emissao=expense_detail.data_emissao,
        data_vencimento=expense_detail.data_vencimento,
        chave_acesso=expense_detail.chave_acesso,
        municipio=expense_detail.municipio
    )

def get_expense_invoices(filters: dict) -> list[ExpenseInvoiceResponseDto]:
    if not filters:
        raise ValueError("No filters provided")
    
    allowed_filters = ["municipio", "data", "codigo_receita", "fonte_recurso"]
    parsed_filters = {}
    for key in filters:
        if key not in allowed_filters:
            raise ValueError(f"Filter {key} not allowed")
        
        if key == "date" and filters[key]:
            parsed_filters[key] = datetime.strptime(filters[key], "%Y-%m-%d")
        elif filters[key]:
            parsed_filters[key] = filters[key]


    try:
        expense_invoice_data = Session.query(ExpenseInvoiceDBModel).filter_by(**parsed_filters).all()
    except Exception as e:
        raise e
        # raise ValueError(f"Error retriving revenue data") from e

    if not expense_invoice_data:
        return None

    return [_db_to_dto(expense_invoice) for expense_invoice in expense_invoice_data]

