from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Expense:
    date: date
    category: str
    cents: int
    note: str = ""
