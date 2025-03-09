from pydantic import BaseModel, Field
from datetime import datetime
from . import constants, base


class RevenueResponseDto(BaseModel):
    id: str
    data: datetime = Field(description=constants.DATA)
    tipo_minuta: str = Field(description=constants.TIPO_MINUTA)
    codigo_receita: str = Field(description=constants.CODIGO_RECEITA)
    descricao_receita: str = Field(description=constants.DESCRICAO_RECEITA)
    fonte_recurso: str = Field(description=constants.FONTE_RECURSO)
    co_tce: str = Field(description=constants.CO_TCE)
    co_aux: str = Field(description=constants.CO_AUX)
    historico: str | None = Field(description=constants.HISTORICO)
    valor: float = Field(description=constants.VALOR)
    municipio: str = Field(description=constants.MUNICIPIO)


class RevenueFilterParams(base.BaseFilterParams):
    municipio: str = Field(None, description=constants.MUNICIPIO)
    data: datetime = Field(None, description=constants.DATA)
    codigo_receita: str = Field(None, description=constants.CODIGO_RECEITA)
    fonte_recurso: str = Field(None, description=constants.FONTE_RECURSO)
