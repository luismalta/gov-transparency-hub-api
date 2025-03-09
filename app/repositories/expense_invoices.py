from app.db.db_models import ExpenseInvoiceDBModel
from app.db.db_connection import Session

from app.dtos.expense_dto import ExpenseInvoiceResponseDto


def _db_to_dto(expense_detail: ExpenseInvoiceDBModel) -> ExpenseInvoiceResponseDto:
    return ExpenseInvoiceResponseDto(
        codigo=expense_detail.codigo,
        tipo=expense_detail.tipo,
        numero_despesa=expense_detail.numero_despesa,
        ano_despesa=expense_detail.ano_despesa,
        nota_fiscal=expense_detail.nota_fiscal,
        serie=expense_detail.serie,
        data_emissao=expense_detail.data_emissao,
        data_vencimento=expense_detail.data_vencimento,
        chave_acesso=expense_detail.chave_acesso,
        municipio=expense_detail.municipio,
    )


def get_expense_invoices(
    filters: dict, pagination_info: dict
) -> list[ExpenseInvoiceResponseDto]:
    try:
        expense_invoice_query = (
            Session.query(ExpenseInvoiceDBModel)
            .filter_by(**filters)
            .order_by(
                ExpenseInvoiceDBModel.data_emissao.desc(),
                ExpenseInvoiceDBModel.municipio,
            )
            .limit(pagination_info["page_size"])
            .offset((pagination_info["page"]) * pagination_info["page_size"])
        )
        expense_invoice_data = expense_invoice_query.all()
    except Exception as e:
        raise e

    if not expense_invoice_data:
        return None

    return [_db_to_dto(expense_invoice) for expense_invoice in expense_invoice_data]
