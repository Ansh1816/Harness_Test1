from datetime import date
from .reader import normalize_category

def select(expenses, start=None, end=None, category=None):
    lower = date.fromisoformat(start) if start else None
    upper = date.fromisoformat(end) if end else None
    if lower and upper and lower > upper:
        raise ValueError("start must not follow end")
    wanted = category.strip() if category is not None else None
    return [e for e in expenses
            if (lower is None or e.date >= lower)
            and (upper is None or e.date < upper)
            and (wanted is None or e.category == wanted)]
