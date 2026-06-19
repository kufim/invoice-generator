from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Party:
    name: str = ""
    address: str = ""

    @classmethod
    def parse(cls, value) -> "Party":
        if isinstance(value, str):
            return cls(name=value)
        value = value or {}
        return cls(name=value.get("name", ""), address=value.get("address", ""))


@dataclass
class LineItem:
    description: str = ""
    quantity: float = 1.0
    rate: float = 0.0

    @property
    def amount(self) -> float:
        return round(self.quantity * self.rate, 2)

    @classmethod
    def parse(cls, data: dict) -> "LineItem":
        return cls(
            description=data.get("description", ""),
            quantity=float(data.get("quantity", 1)),
            rate=float(data.get("rate", 0)),
        )


@dataclass
class Invoice:
    number: str = "1"
    sender: Party = field(default_factory=Party)
    bill_to: Party = field(default_factory=Party)
    ship_to: Party = field(default_factory=Party)
    date: str = ""
    payment_terms: str = ""
    due_date: str = ""
    po_number: str = ""
    items: list[LineItem] = field(default_factory=list)
    notes: str = ""
    terms: str = ""
    tax_rate: float = 0.0
    discount: float = 0.0
    shipping: float = 0.0
    amount_paid: float = 0.0
    currency: str = "$"
    logo: str | None = None

    @classmethod
    def parse(cls, data: dict) -> "Invoice":
        return cls(
            number=str(data.get("number", "1")),
            sender=Party.parse(data.get("from")),
            bill_to=Party.parse(data.get("bill_to")),
            ship_to=Party.parse(data.get("ship_to")),
            date=data.get("date", ""),
            payment_terms=data.get("payment_terms", ""),
            due_date=data.get("due_date", ""),
            po_number=data.get("po_number", ""),
            items=[LineItem.parse(item) for item in data.get("items", [])],
            notes=data.get("notes", ""),
            terms=data.get("terms", ""),
            tax_rate=float(data.get("tax_rate", 0)),
            discount=float(data.get("discount", 0)),
            shipping=float(data.get("shipping", 0)),
            amount_paid=float(data.get("amount_paid", 0)),
            currency=data.get("currency", "$"),
            logo=data.get("logo"),
        )