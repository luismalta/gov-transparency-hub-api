from datetime import datetime
from app.db.db_models import ExpenseDetailDBModel
from app.db.db_connection import Session

from app.dtos.expense_dto import ExpenseDetailsResponseDto

def _db_to_dto(expense_detail: ExpenseDetailDBModel) -> ExpenseDetailsResponseDto:
    return ExpenseDetailsResponseDto(
        numero=expense_detail.numero,
        ano=expense_detail.ano,
        tipo=expense_detail.tipo,
        data_empenho=expense_detail.data_empenho,
        data_liquidacao=expense_detail.data_liquidacao,
        data_pagamento=expense_detail.data_pagamento,
        unidade=expense_detail.unidade,
        funcao=expense_detail.funcao,
        subfuncao=expense_detail.subfuncao,
        programa=expense_detail.programa,
        atividade=expense_detail.atividade,
        categoria_economica=expense_detail.categoria_economica,
        fonte_recurso=expense_detail.fonte_recurso,
        co_tce=expense_detail.co_tce,
        co_aux=expense_detail.co_aux,
        valor=expense_detail.valor,
        beneficiario=expense_detail.beneficiario,
        cpf_cnpj=expense_detail.cpf_cnpj,
        historico=expense_detail.historico,
        municipio=expense_detail.municipio
    )

def get_expense_details(filters: dict) -> list[ExpenseDetailsResponseDto]:
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
        expense_detail_data = Session.query(ExpenseDetailDBModel).filter_by(**parsed_filters).all()
    except Exception as e:
        raise e
        # raise ValueError(f"Error retriving revenue data") from e

    if not expense_detail_data:
        return None

    return [_db_to_dto(expense_detail) for expense_detail in expense_detail_data]

