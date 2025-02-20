from datetime import datetime
from app.db.db_models import RevenueDBModel
from app.db.db_connection import Session

from app.dtos.revenue_dto import RevenueResponseDto

def _db_to_dto(revenue: RevenueDBModel) -> RevenueResponseDto:
    return RevenueResponseDto(
        id=revenue.id,
        data=revenue.data,
        tipo_minuta=revenue.tipo_minuta,
        codigo_receita=revenue.codigo_receita,
        descricao_receita=revenue.descricao_receita,
        fonte_recurso=revenue.fonte_recurso,
        co_tce=revenue.co_tce,
        co_aux=revenue.co_aux,
        historico=revenue.historico,
        valor=revenue.valor,
        municipio=revenue.municipio
    )

def get_revenue(filters: dict) -> list[RevenueResponseDto]:
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
        revenue_data = Session.query(RevenueDBModel).filter_by(**parsed_filters).all()
    except Exception as e:
        raise e
        # raise ValueError(f"Error retriving revenue data") from e

    if not revenue_data:
        return None

    return [_db_to_dto(revenue) for revenue in revenue_data]

