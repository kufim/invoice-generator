from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .models import Invoice
from .renderer import render_pdf


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="invoicegen",
        description="Generate a polished PDF invoice from a JSON file.",
    )
    parser.add_argument("source", help="path to the invoice JSON file")
    parser.add_argument("-o", "--output", help="output PDF path (default: invoice_<number>.pdf)")
    args = parser.parse_args(argv)

    source = Path(args.source)
    if not source.exists():
        print(f"error: file not found: {source}", file=sys.stderr)
        return 1

    try:
        data = json.loads(source.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"error: invalid JSON in {source}: {exc}", file=sys.stderr)
        return 1

    invoice = Invoice.parse(data)
    output = Path(args.output) if args.output else Path(f"invoice_{invoice.number}.pdf")
    render_pdf(invoice, output)
    print(f"Wrote {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())