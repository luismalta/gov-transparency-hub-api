from datetime import datetime
from sqlalchemy import String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class RevenueDBModel(Base):
    __tablename__ = 'revenue_details'

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