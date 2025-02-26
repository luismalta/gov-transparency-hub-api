from datetime import datetime
from app.db.db_models import ExpenseItemDBModel
from app.db.db_connection import Session

from app.dtos.expense_dto import ExpenseItemResponseDto

def _db_to_dto(expense_detail: ExpenseItemDBModel) -> ExpenseItemResponseDto:
    return ExpenseItemResponseDto(
        item=expense_detail.item,
        numero=expense_detail.numero_despesa,
        ano=expense_detail.ano_despesa,
        municipio=expense_detail.municipio,
        complemento=expense_detail.complemento,
        unidade=expense_detail.unidade,
        marca=expense_detail.marca,
        quantidade=expense_detail.quantidade,
        valor_unitario=expense_detail.valor_unitario,
        valor_total=expense_detail.total
    )

def get_expense_itens(filters: dict) -> list[ExpenseItemResponseDto]:
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
        expense_itens_data = Session.query(ExpenseItemDBModel).filter_by(**parsed_filters).all()
    except Exception as e:
        raise e
        # raise ValueError(f"Error retriving revenue data") from e

    if not expense_itens_data:
        return None

    return [_db_to_dto(expense_item) for expense_item in expense_itens_data]

