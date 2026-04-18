from __future__ import annotations

import csv
import json
from pathlib import Path


FIELDS = ["rank", "name", "youtube", "linkedin"]


def get_dummy_experts() -> list[dict[str, object]]:
    return [
        {
            "rank": 1,
            "name": "Alex Morgan",
            "youtube": "https://youtube.com/@alexmorgan",
            "linkedin": "https://linkedin.com/in/alexmorgan",
        },
        {
            "rank": 2,
            "name": "Sarah Kim",
            "youtube": "https://youtube.com/@sarahkim",
            "linkedin": "https://linkedin.com/in/sarahkim",
        },
        {
            "rank": 3,
            "name": "Daniel Brooks",
            "youtube": "https://youtube.com/@danielbrooks",
            "linkedin": "https://linkedin.com/in/danielbrooks",
        },
        {
            "rank": 4,
            "name": "Emma Carter",
            "youtube": "https://youtube.com/@emmacarter",
            "linkedin": "https://linkedin.com/in/emmacarter",
        },
        {
            "rank": 5,
            "name": "Ryan Lee",
            "youtube": "https://youtube.com/@ryanlee",
            "linkedin": "https://linkedin.com/in/ryanlee",
        },
        {
            "rank": 6,
            "name": "Olivia Smith",
            "youtube": "https://youtube.com/@oliviasmith",
            "linkedin": "https://linkedin.com/in/oliviasmith",
        },
        {
            "rank": 7,
            "name": "Jason Miller",
            "youtube": "https://youtube.com/@jasonmiller",
            "linkedin": "https://linkedin.com/in/jasonmiller",
        },
        {
            "rank": 8,
            "name": "Sophia White",
            "youtube": "https://youtube.com/@sophiawhite",
            "linkedin": "https://linkedin.com/in/sophiawhite",
        },
        {
            "rank": 9,
            "name": "David Wilson",
            "youtube": "https://youtube.com/@davidwilson",
            "linkedin": "https://linkedin.com/in/davidwilson",
        },
        {
            "rank": 10,
            "name": "Mia Johnson",
            "youtube": "https://youtube.com/@miajohnson",
            "linkedin": "https://linkedin.com/in/miajohnson",
        },
    ]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in FIELDS})


def write_json(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
        f.write("\n")


def write_markdown(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write("# Top 10 Experts\n\n")
        f.write("| rank | name | youtube | linkedin |\n")
        f.write("|---:|---|---|---|\n")
        for row in rows:
            f.write(
                f"| {row['rank']} | {row['name']} | {row['youtube']} | {row['linkedin']} |\n"
            )


def main() -> int:
    experts = get_dummy_experts()
    output_root = Path.cwd()

    write_csv(output_root / "result/exports/experts.csv", experts)
    write_json(output_root / "result/exports/experts.json", experts)
    write_markdown(output_root / "result/summaries/experts.md", experts)

    print("Done! Generated experts exports in result/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
