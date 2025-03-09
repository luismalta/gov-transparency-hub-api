from datetime import datetime
from sqlalchemy import String, Float, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class RevenueDBModel(Base):
    __tablename__ = "revenue_details"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    data: Mapped[datetime] = mapped_column(DateTime)
    tipo_minuta: Mapped[str] = mapped_column(String, comment="Tipo de minuta desc")
    codigo_receita: Mapped[str] = mapped_column(String)
    descricao_receita: Mapped[str] = mapped_column(String)
    fonte_recurso: Mapped[str] = mapped_column(String)
    co_tce: Mapped[str] = mapped_column(String)
    co_aux: Mapped[str] = mapped_column(String)
    historico: Mapped[str] = mapped_column(String)
    valor: Mapped[float] = mapped_column(Float)
    municipio: Mapped[str] = mapped_column(String)


class ExpenseDetailDBModel(Base):
    __tablename__ = "expense_details"

    numero: Mapped[str] = mapped_column(String, primary_key=True)
    ano: Mapped[int] = mapped_column(Integer, primary_key=True)
    municipio: Mapped[str] = mapped_column(String, primary_key=True)
    tipo: Mapped[str] = mapped_column(String)
    data_empenho: Mapped[datetime] = mapped_column(DateTime)
    data_liquidacao: Mapped[datetime] = mapped_column(DateTime)
    data_pagamento: Mapped[datetime] = mapped_column(DateTime)
    unidade: Mapped[str] = mapped_column(String)
    funcao: Mapped[str] = mapped_column(String)
    subfuncao: Mapped[str] = mapped_column(String)
    programa: Mapped[str] = mapped_column(String)
    atividade: Mapped[str] = mapped_column(String)
    categoria_economica: Mapped[str] = mapped_column(String)
    fonte_recurso: Mapped[str] = mapped_column(String)
    co_tce: Mapped[str] = mapped_column(String)
    co_aux: Mapped[str] = mapped_column(String)
    valor: Mapped[float] = mapped_column(Float)
    beneficiario: Mapped[str] = mapped_column(String)
    cpf_cnpj: Mapped[str] = mapped_column(String)
    historico: Mapped[str] = mapped_column(String)


class ExpenseItemDBModel(Base):
    __tablename__ = "expense_itens"

    item: Mapped[str] = mapped_column(String, primary_key=True)
    numero_despesa: Mapped[str] = mapped_column(String, primary_key=True)
    ano_despesa: Mapped[int] = mapped_column(Integer, primary_key=True)
    municipio: Mapped[str] = mapped_column(String, primary_key=True)
    complemento: Mapped[str] = mapped_column(String)
    unidade: Mapped[str] = mapped_column(String)
    marca: Mapped[str] = mapped_column(String)
    quantidade: Mapped[float] = mapped_column(Float)
    valor_unitario: Mapped[float] = mapped_column(Float)
    total: Mapped[float] = mapped_column(Float)


class ExpenseInvoiceDBModel(Base):
    __tablename__ = "expense_invoices"

    ano_despesa: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero_despesa: Mapped[str] = mapped_column(String, primary_key=True)
    municipio: Mapped[str] = mapped_column(String, primary_key=True)
    codigo: Mapped[str] = mapped_column(String)
    tipo: Mapped[str] = mapped_column(String)
    nota_fiscal: Mapped[str] = mapped_column(String)
    serie: Mapped[str] = mapped_column(String)
    data_emissao: Mapped[datetime] = mapped_column(DateTime)
    data_vencimento: Mapped[datetime] = mapped_column(DateTime)
    chave_acesso: Mapped[str] = mapped_column(String)
