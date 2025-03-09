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

def get_revenue(filters: dict, pagination_info: dict) -> list[RevenueResponseDto]:
    try:
        revenue_query = Session.query(RevenueDBModel)\
            .filter_by(**filters)\
            .order_by(RevenueDBModel.data.desc(), RevenueDBModel.municipio)\
            .limit(pagination_info["page_size"])\
            .offset((pagination_info["page"]) * pagination_info["page_size"])
        revenue_data = revenue_query.all()
    except Exception as e:
        raise e

    if not revenue_data:
        return None

    return [_db_to_dto(revenue) for revenue in revenue_data]

