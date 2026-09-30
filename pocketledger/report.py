def summarize(expenses):
    rows = list(expenses)
    categories = {}
    for expense in rows:
        categories[expense.category] = categories.get(expense.category, 0) + expense.cents
    return {"count": len(rows), "total_cents": sum(abs(e.cents) for e in rows),
            "by_category": dict(sorted(categories.items()))}
