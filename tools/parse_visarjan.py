"""Parse MPPCB idol-immersion report text (pdftotext -layout) into a long CSV.

Usage: python3 -I parse_visarjan.py <report.txt> <year> <out.csv>

Works on the 2023, 2024 and 2025 layouts. Every table is: a site-name line
(with or without a 'Location-' prefix), a header line with Pre / During / After
columns, then numbered parameter rows. Pages are separated by form feeds."""
import csv, re, sys

src, year, out = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(src, encoding="utf-8", errors="replace").read()

PARAM = re.compile(r"^\s*(\d{1,2})\s+([A-Za-z][A-Za-z .\-/()]*?)\s{2,}(\S.*)$")
TOKEN = re.compile(r"\S+")
SKIP = re.compile(r"water (quality )?monitoring report|idol immersion|visarjan 20\d\d|^\s*r\.?o\.?\b|^\s*20\d\d(\s+20\d\d)*\s*$|s\.\s*no", re.I)

def clean_site(line):
    s = line.strip()
    s = re.split(r"\s{3,}", s)[0]            # drop a right-aligned 'R.O. Bhopal'
    s = re.sub(r"^location\s*[-:]\s*", "", s, flags=re.I)
    return s.strip().rstrip(".").strip()

rows, festival, ro, miss = [], "", "", 0
recent, cols, site = [], None, None
for page_no, page in enumerate(text.split("\f"), start=1):
    for line in page.split("\n"):
        low = line.lower()
        if re.search(r"ganesh[a]?\s+(idol|visarjan)", low): festival = "Ganesh"
        if re.search(r"durga\s+(idol|visarjan)", low) and "location" not in low: festival = "Durga"
        m = re.search(r"\b(R\.\s?O\.?\s*[-:]?\s*[A-Z][a-z]+|RO-[A-Z][a-z]+)", line)
        if m: ro = re.sub(r"\s+", " ", m.group(1)).replace("RO-", "R.O. ").strip()

        if re.search(r"pre\s*immersion", low) and "during" in low:
            # Header row. The site is the nearest earlier line that is not a heading.
            loc = [l for l in recent if "location" in l.lower()]
            cand = [l for l in recent if l.strip() and not SKIP.search(l)]
            site = clean_site(loc[-1] if loc else (cand[-1] if cand else "UNKNOWN"))
            cols = [c for c in (low.find("pre"), low.find("during"), low.find("after")) if c >= 0]
            recent, miss = [], 0
            continue

        if cols:
            m = PARAM.match(line)
            if m:
                names = ["pre", "during", "after"][:len(cols)]
                vals, base = {}, m.start(3)
                for t in TOKEN.finditer(m.group(3)):
                    d = [abs(t.start() + base - c) for c in cols]
                    vals.setdefault(names[d.index(min(d))], t.group())
                for ph in names:
                    raw = vals.get(ph, "")
                    try:
                        num, flag = float(raw), ""
                    except ValueError:
                        num, flag = "", (raw if raw not in ("", "_", "-") else "not sampled")
                    rows.append(dict(year=year, festival=festival, regional_office=ro,
                                     site_as_printed=site, phase=ph,
                                     parameter=m.group(2).strip(), value=num,
                                     value_as_printed=raw, flag=flag, source_page=page_no))
                miss = 0
                continue
            # A table ends after two non-parameter text lines in a row, so a single
            # 'S.No. Parameter' or year row under the header does not end it.
            if line.strip() and not SKIP.search(line):
                miss += 1
                if miss >= 2:
                    cols = None
        recent = (recent + [line])[-6:]

if not rows:
    # Guard: a new report layout yields zero tables. Fail loudly instead of writing an empty CSV.
    sys.exit(f"No tables parsed from {src}. Layout differs from the known 2023-2025 reports.")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
tables = {(r["festival"], r["site_as_printed"], r["source_page"]) for r in rows}
print(f"{src.split('/')[-1]}: {len(rows)} rows, {len(tables)} tables")
