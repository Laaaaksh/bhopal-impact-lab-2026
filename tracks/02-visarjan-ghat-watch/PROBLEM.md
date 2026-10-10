# Track 2: Visarjan Ghat Watch

**Turn three years of buried water tests into a warning Bhopal can act on before Durga visarjan.**

## The problem

Every Ganesh and Durga festival, the MP Pollution Control Board tests the water at Bhopal's idol-immersion ghats three times: before immersion, during, and one week after. The results go into reports of 90 to 120 pages. Nobody lines them up against the legal limits or compares one year with the next.

The numbers inside those reports are alarming:

- At **Bairagarh (Sant Hirdaram) kund**, dissolved oxygen read **0 mg/l** four times across 2023 and 2025. Water at zero oxygen supports no fish life at all. The bathing-water standard asks for at least 5.
- Across all Bhopal ghat readings from 2023 to 2025, **42 of 116 dissolved-oxygen readings fall below 5 mg/l**, and **100 of 112 BOD readings sit above the bathing limit of 3 mg/l**.

The National Green Tribunal has banned immersion in the Upper and Lower Lakes. Bhopal Municipal Corporation is building new ghats. **Durga visarjan falls on 20 October 2026, nine days after this event.**

## Your user

**The Bhopal Municipal Corporation officer who plans Durga visarjan at the ghats.** This officer decides where to send extra cleaning, aeration and water testing. Today that decision rests on memory, because the test results sit in PDFs nobody reads.

## The data

Everything sits in `data/` and `resources/` in this folder.

| File | What it holds |
|---|---|
| `data/bhopal_ghats_2023_2025.csv` | **Start here.** Every reading at 7 Bhopal ghats, 2023 to 2025, Ganesh and Durga, before / during / after. 1,524 rows. Spot-checked against the PDFs |
| `data/sample_bhopal_2025.csv` | The 2025 readings only, for quick testing |
| `data/mp_immersion_sites_2023_2025.csv` | The same tests for about 200 sites across MP. 21,600 rows. Less checked. Rows marked `needs_check` have no readable site name |
| `data/cpcb_water_quality_criteria.csv` | The official CPCB water-quality limits (classes A to E) |
| `resources/` | The original MPPCB reports (2023, 2024, 2025) and Upper / Lower Lake monthly water-quality reports |

Read `data/DATA_DICTIONARY.md` before you start. It explains BDL, blanks and the units.

## What "done" looks like

A working tool that gives the BMC officer, before 20 October:

1. A **ranked list of Bhopal ghats** by risk, with the reason for each rank in plain words.
2. The **numbers behind every rank**, traceable to the report and page.
3. A short **brief in Hindi and English** the officer can forward.

A strong submission also shows what changed across 2023, 2024 and 2025, and says honestly where the data is missing.

## Starting points

These are ideas, not instructions. Pick your own approach.

- Decide which CPCB class fits immersion ghats, and say why. Class B (outdoor bathing) is a reasonable start.
- Only 4 to 6 metals were tested. Your tool reports what was tested. It does not guess the rest.
- Some ghats were sampled only during immersion. A blank is "not sampled", not "clean".
- One site name ("Rani Kamlapati ghat / Kamla Park kund") may cover two places. Check `site_match_confidence`.
- Your non-technical teammates matter here: researching the NGT order and CPCB guidelines, placing the ghats on a map, writing the Hindi brief, checking numbers against the PDFs.

## Constraints

- Public data only. Everything you need is in this folder.
- No connection to any live government system.
- Do not claim health effects the data does not show. Report the readings against the limits.

## Sources

- MPPCB Ganesh and Durga Visarjan Reports 2025, 2024 and 2023: https://www.mppcb.mp.gov.in/proc/mon/ (files listed in `data/DATA_DICTIONARY.md`, downloaded 10 Oct 2026)
- CPCB water quality criteria: https://cpcb.gov.in/water-quality-criteria/ (read 10 Oct 2026)
- NGT immersion ban and new BMC ghats, Free Press Journal, 26 Feb 2026: https://www.freepressjournal.in/amp/bhopal/mp-news-idol-immersion-to-shift-from-lakes-to-safer-sites-ngt-ban-pushes-bmc-to-build-4-dedicated-ghats
- Durga visarjan date 20 Oct 2026, Drik Panchang: https://www.drikpanchang.com/navratri/durga-puja/durga-visarjan-date-time.html?year=2026
