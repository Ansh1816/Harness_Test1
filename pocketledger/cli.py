import argparse
import json
from pathlib import Path
from .reader import read_expenses
from .filters import select
from .report import summarize

def main():
    parser = argparse.ArgumentParser(description="Summarize CSV expenses")
    parser.add_argument("file", nargs="?")
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--start")
    parser.add_argument("--end")
    parser.add_argument("--category")
    args = parser.parse_args()
    path = Path(__file__).resolve().parent.parent / "sample.csv" if args.demo else args.file
    if not path:
        parser.error("provide a CSV file or --demo")
    expenses = read_expenses(Path(path).read_text(encoding="utf-8"))
    result = summarize(select(expenses, args.start, args.end, args.category))
    print(json.dumps(result, sort_keys=True))
