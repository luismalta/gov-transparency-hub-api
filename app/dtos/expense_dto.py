from pydantic import BaseModel
from datetime import datetime

class ExpenseDetailsResponseDto(BaseModel):
    numero: str
    ano: str
    tipo: str
    data_empenho: datetime
    data_liquidacao: datetime | None 
    data_pagamento: datetime | None
    unidade: str
    funcao: str
    subfuncao: str
    programa: str
    atividade: str
    categoria_economica: str
    fonte_recurso: str
    co_tce: str
    co_aux: str
    valor: float
    beneficiario: str
    cpf_cnpj: str
    historico: str
    municipio: str

class ExpenseItemResponseDto(BaseModel):
    item: str
    numero_despesa: str
    ano_despesa: str
    municipio: str
    complemento: str | None
    unidade: str
    marca: str | None
    quantidade: float
    valor_unitario: float
    valor_total: float

class ExpenseInvoiceResponseDto(BaseModel):
    ano_despesa: str
    numero_despesa: str
    municipio: str
    codigo: str
    tipo: str
    nota_fiscal: str
    serie: str
    data_emissao: datetime
    data_vencimento: datetime
    chave_acesso: str
    