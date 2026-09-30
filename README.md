# PocketLedger

A small expense-reporting CLI. Import CSV expenses, filter by date and category,
and generate a JSON summary. Credits are represented by negative amounts.
Python 3.9+; no dependencies, account, database, or network required.

```sh
make setup
make demo
make test
python3 -m pocketledger sample.csv --start 2026-09-01 --end 2026-09-30
python3 -m pocketledger sample.csv --category travel
```

Flow: CLI → CSV reader → Expense records → filters → summary → JSON.
`pocketledger/` contains the application; `tests/` contains executable expectations.
The precise data contract is in [docs/behavior.md](docs/behavior.md).

This is a debugging exercise snapshot. Some tests intentionally fail initially.
Repair application behavior according to the contract, retaining the existing tests.
