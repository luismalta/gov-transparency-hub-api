from app.db.db_models import ExpenseItemDBModel
from app.db.db_connection import Session

from app.dtos.expense_dto import ExpenseItemResponseDto


def _db_to_dto(expense_detail: ExpenseItemDBModel) -> ExpenseItemResponseDto:
    return ExpenseItemResponseDto(
        item=expense_detail.item,
        numero_despesa=expense_detail.numero_despesa,
        ano_despesa=expense_detail.ano_despesa,
        municipio=expense_detail.municipio,
        complemento=expense_detail.complemento,
        unidade=expense_detail.unidade,
        marca=expense_detail.marca,
        quantidade=expense_detail.quantidade,
        valor_unitario=expense_detail.valor_unitario,
        valor_total=expense_detail.total,
    )


def get_expense_itens(
    filters: dict, pagination_info: dict
) -> list[ExpenseItemResponseDto]:
    try:
        expense_itens_query = (
            Session.query(ExpenseItemDBModel)
            .filter_by(**filters)
            .order_by(
                ExpenseItemDBModel.numero_despesa.desc(), ExpenseItemDBModel.municipio
            )
            .limit(pagination_info["page_size"])
            .offset((pagination_info["page"]) * pagination_info["page_size"])
        )
        expense_itens_data = expense_itens_query.all()
    except Exception as e:
        raise e

    if not expense_itens_data:
        return None

    return [_db_to_dto(expense_item) for expense_item in expense_itens_data]
