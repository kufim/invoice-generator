from __future__ import annotations

from .models import Invoice


def subtotal(invoice: Invoice) -> float:
    return round(sum(item.amount for item in invoice.items), 2)


def tax_amount(invoice: Invoice) -> float:
    return round(subtotal(invoice) * invoice.tax_rate / 100, 2)


def total(invoice: Invoice) -> float:
    return round(subtotal(invoice) + tax_amount(invoice) - invoice.discount + invoice.shipping, 2)


def balance_due(invoice: Invoice) -> float:
    return round(total(invoice) - invoice.amount_paid, 2)


def summary(invoice: Invoice) -> dict:
    return {
        "subtotal": subtotal(invoice),
        "tax": tax_amount(invoice),
        "discount": round(invoice.discount, 2),
        "shipping": round(invoice.shipping, 2),
        "total": total(invoice),
        "amount_paid": round(invoice.amount_paid, 2),
        "balance_due": balance_due(invoice),
    }