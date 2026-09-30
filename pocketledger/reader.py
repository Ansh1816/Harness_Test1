import csv
import io
from datetime import date
from .models import Expense
from .money import to_cents

def normalize_category(value):
    category = value.strip().casefold()
    if not category:
        raise ValueError("category is required")
    return category

def read_expenses(text):
    lines = text.strip().splitlines()
    rows = [dict(zip(lines[0].split(","), line.split(","))) for line in lines[1:]]
    return [Expense(date.fromisoformat(row["date"]),
                    normalize_category(row["category"]),
                    to_cents(row["amount"]), row.get("note", "")) for row in rows]
