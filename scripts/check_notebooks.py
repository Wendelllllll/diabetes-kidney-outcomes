"""Validate committed notebook source without executing restricted-data queries."""
import ast
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    problems = []
    notebooks = sorted((root / "notebooks").glob("*.ipynb"))
    for path in notebooks:
        notebook = json.loads(path.read_text())
        for index, cell in enumerate(notebook["cells"], start=1):
            label = f"{path.name}, cell {index}"
            if cell.get("attachments"):
                problems.append(f"{label}: embedded attachments")
            if cell.get("outputs") or cell.get("execution_count") is not None:
                problems.append(f"{label}: saved output or execution state")
            if cell.get("metadata"):
                problems.append(f"{label}: unexpected cell metadata")
            if cell["cell_type"] == "code":
                try:
                    ast.parse("".join(cell["source"]))
                except SyntaxError as error:
                    problems.append(f"{label}: {error}")
    if not notebooks:
        problems.append("No notebooks found")
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"Validated {len(notebooks)} notebooks: syntax OK, no saved outputs or attachments.")


if __name__ == "__main__":
    main()

