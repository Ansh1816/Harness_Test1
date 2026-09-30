from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

def to_cents(value):
    try:
        amount = Decimal(value)
        if not amount.is_finite():
            raise ValueError("amount must be finite")
        return int(amount * 100)
    except (InvalidOperation, TypeError) as exc:
        raise ValueError("invalid amount") from exc
