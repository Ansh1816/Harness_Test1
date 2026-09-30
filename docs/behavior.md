# Data and reporting contract

CSV columns are `date,category,amount,note`. CSV follows standard quoting rules:
a note may contain commas, quotes, or newlines. Dates are ISO YYYY-MM-DD.
Categories are trimmed and case-folded when read and when queried.
Monetary input is a finite decimal string, rounded to integer cents using
decimal ROUND_HALF_UP (ties away from zero). Never use binary float for money.
Negative amounts are credits and reduce totals. Empty category and invalid
dates or amounts raise ValueError.

`read_expenses(text)` returns Expense records with date, category, cents, note.
`select(expenses, start=None, end=None, category=None)` includes both date
endpoints and preserves input order. A same-day range includes that day.
A reversed range raises ValueError. Selection must not mutate its input.
`summarize(expenses)` returns count, total_cents, and by_category. Category
totals and the overall total are signed net sums, including credits. Empty
input returns count=0, total_cents=0, and an empty by_category object.
The CLI uses exactly these functions and emits one JSON object.
