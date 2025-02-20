from pydantic import BaseModel
from datetime import datetime

class RevenueResponseDto(BaseModel):
    id: str
    data: datetime
    tipo_minuta: str
    codigo_receita: str
    descricao_receita: str
    fonte_recurso: str
    co_tce: str
    co_aux: str
    historico: str
    valor: float
    municipio: str