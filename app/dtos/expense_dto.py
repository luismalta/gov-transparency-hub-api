from pydantic import BaseModel, Field
from datetime import datetime
from . import constants, base

class ExpenseDetailsResponseDto(BaseModel):
    numero: str = Field(description=constants.NUMERO_EMPENHO)
    ano: str = Field(description=constants.ANO_DESPESA)
    tipo: str = Field(description=constants.TIPO_DESPESA)
    data_empenho: datetime = Field(description=constants.DATA_EMPENHO)
    data_liquidacao: datetime | None  = Field(description=constants.DATA_LIQUIDACAO)
    data_pagamento: datetime | None = Field(description=constants.DATA_PAGAMENTO)
    unidade: str = Field(description=constants.UNIDADE)
    funcao: str = Field(description=constants.FUNCAO)
    subfuncao: str = Field(description=constants.SUBFUNCAO)
    programa: str = Field(description=constants.PROGRAMA)
    atividade: str = Field(description=constants.ATIVIDADE)
    categoria_economica: str = Field(description=constants.CATEGORIA_ECONOMICA)
    fonte_recurso: str = Field(description=constants.FONTE_RECURSO)
    co_tce: str = Field(description=constants.CO_TCE)
    co_aux: str = Field(description=constants.CO_AUX)
    valor: float = Field(description=constants.VALOR_DESPESA)
    beneficiario: str = Field(description=constants.BENEFICIARIO)
    cpf_cnpj: str = Field(description=constants.CPF_CNPJ)
    historico: str = Field(description=constants.HISTORICO_DESPESA)
    municipio: str = Field(description=constants.MUNICIPIO_DESPESA)

class ExpenseItemResponseDto(BaseModel):
    item: str = Field(description=constants.ITEM_DESPESA)
    numero_despesa: str = Field(description=constants.NUMERO_DESPESA_ITEM)
    ano_despesa: str = Field(description=constants.ANO_DESPESA)
    municipio: str = Field(description=constants.MUNICIPIO_DESPESA)
    complemento: str | None = Field(description=constants.COMPLEMENTO_ITEM_DESPESA)
    unidade: str = Field(description=constants.UNIDADE_ITEM)
    marca: str | None = Field(description=constants.MARCA_ITEM)
    quantidade: float = Field(description=constants.QUANTIDADE_ITEM)
    valor_unitario: float = Field(description=constants.VALOR_UNITARIO_ITEM)
    valor_total: float = Field(description=constants.VALOR_TOTAL_ITEM)

class ExpenseInvoiceResponseDto(BaseModel):
    ano_despesa: str = Field(description=constants.ANO_DESPESA_NF)
    numero_despesa: str = Field(description=constants.NUMERO_DESPESA_NF)
    municipio: str = Field(description=constants.MUNICIPIO_NF)
    codigo: str = Field(description=constants.CODIGO_NF)
    tipo: str = Field(description=constants.TIPO_NF)
    nota_fiscal: str = Field(description=constants.NOTA_FISCAL)
    serie: str = Field(description=constants.SERIE_NF)
    data_emissao: datetime = Field(description=constants.DATA_EMISSAO_NF)
    data_vencimento: datetime = Field(description=constants.DATA_VENCIMENTO_NF)
    chave_acesso: str | None = Field(description=constants.CHAVE_ACESSO_NF)


class ExpenseDetailsFilterParams(base.BaseFilterParams):
    municipio: str = Field(None, description=constants.MUNICIPIO_DESPESA)
    ano: str = Field(None, description=constants.ANO_DESPESA)
    numero: str = Field(None, description=constants.NUMERO_EMPENHO)
    tipo: str = Field(None, description=constants.TIPO_DESPESA)
    data_empenho: datetime = Field(None, description=constants.DATA_EMPENHO)
    data_liquidacao: datetime = Field(None, description=constants.DATA_LIQUIDACAO)
    data_pagamento: datetime = Field(None, description=constants.DATA_PAGAMENTO)
    unidade: str = Field(None, description=constants.UNIDADE)
    funcao: str = Field(None, description=constants.FUNCAO)
    subfuncao: str = Field(None, description=constants.SUBFUNCAO)
    programa: str = Field(None, description=constants.PROGRAMA)
    atividade: str = Field(None, description=constants.ATIVIDADE)
    categoria_economica: str = Field(None, description=constants.CATEGORIA_ECONOMICA)
    fonte_recurso: str = Field(None, description=constants.FONTE_RECURSO)
    co_tce: str = Field(None, description=constants.CO_TCE)
    co_aux: str = Field(None, description=constants.CO_AUX)
    beneficiario: str = Field(None, description=constants.BENEFICIARIO)
    cpf_cnpj: str = Field(None, description=constants.CPF_CNPJ)
    historico: str = Field(None, description=constants.HISTORICO_DESPESA)


class ExpenseItemFilterParams(base.BaseFilterParams):
    municipio: str = Field(None, description=constants.MUNICIPIO_DESPESA)
    ano_despesa: str = Field(None, description=constants.ANO_DESPESA)
    numero_despesa: str = Field(None, description=constants.NUMERO_DESPESA_ITEM)
    item: str = Field(None, description=constants.ITEM_DESPESA)


class ExpenseInvoiceFilterParams(base.BaseFilterParams):
    municipio: str = Field(None, description=constants.MUNICIPIO_NF)
    ano_despesa: str = Field(None, description=constants.ANO_DESPESA_NF)
    numero_despesa: str = Field(None, description=constants.NUMERO_DESPESA_NF)
    codigo: str = Field(None, description=constants.CODIGO_NF)
    tipo: str = Field(None, description=constants.TIPO_NF)
    nota_fiscal: str = Field(None, description=constants.NOTA_FISCAL)
    serie: str = Field(None, description=constants.SERIE_NF)
    data_emissao: datetime = Field(None, description=constants.DATA_EMISSAO_NF)
    data_vencimento: datetime = Field(None, description=constants.DATA_VENCIMENTO_NF)
    chave_acesso: str = Field(None, description=constants.CHAVE_ACESSO_NF)