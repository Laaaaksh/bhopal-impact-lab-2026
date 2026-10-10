# Tools

The scripts that made the cleaned data in `tracks/`. You do not need them to build. They are here so anyone can check how the data was made, or rerun it on next year's reports.

Both need `pdftotext` (from Poppler) and Python 3. No other packages.

| Script | What it does | Run |
|---|---|---|
| `split_rules.py` | Splits the Bhumi Vikas Rules into one JSON record per rule, with page numbers | `pdftotext -layout rules.pdf rules.txt` then `python3 split_rules.py rules.txt out.jsonl` |
| `parse_visarjan.py` | Turns every table in an MPPCB immersion report into CSV rows | `pdftotext -layout report.pdf report.txt` then `python3 parse_visarjan.py report.txt 2025 out.csv` |

Both scripts stop with an error if the output looks wrong (too few rules, or no tables), instead of writing an empty file.

After parsing, two small mappings were applied by hand:

- Parameter names standardised (`D.Oxygen` and `D. Oxygen` became `Dissolved oxygen`, `suspended-solids` became `Suspended solids`) and a standard unit added.
- Bhopal site names mapped to 7 standard ghat names, with a confidence column.

Both mappings are listed in `tracks/02-visarjan-ghat-watch/data/DATA_DICTIONARY.md`.
