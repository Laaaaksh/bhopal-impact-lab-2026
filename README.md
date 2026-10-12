# Claude Impact Lab, Bhopal

**Sunday 11 October 2026 · Build day · Bhopal**

Welcome. Today you build a working tool for a real Bhopal problem, in one day, with Claude and Claude Code. Everything you build is open source and offered to the Government of Madhya Pradesh through MPSeDC.

This repo holds everything you need: the problems, the data, the rules, the schedule, and how you are judged.

---

## Pick one of two tracks

| | Track 1: Bhumi Vikas Sahayak | Track 2: Visarjan Ghat Watch |
|---|---|---|
| **In one line** | Ask the Bhopal building rulebook and get an answer with the rule number | Turn three years of ghat water tests into a risk warning before Durga visarjan |
| **User** | Building-permission clerk, Bhopal Municipal Corporation | BMC officer planning Durga visarjan at the ghats |
| **Data** | 105 rules from the MP Bhumi Vikas Rules 2012, split and page-referenced | 1,524 water-test readings at 7 Bhopal ghats, 2023 to 2025 |
| **Problem shape** | Ask the rulebook | Messy reports into a clean record and a recurring brief |
| **Read** | [tracks/01-bhumi-vikas-sahayak/PROBLEM.md](tracks/01-bhumi-vikas-sahayak/PROBLEM.md) | [tracks/02-visarjan-ghat-watch/PROBLEM.md](tracks/02-visarjan-ghat-watch/PROBLEM.md) |

Your team picks one track at the opening. Organisers may ask a few teams to switch so both tracks have builders.

## Schedule (Sunday 11 October)

| Time | What happens |
|---|---|
| 09:00 | Check-in and breakfast |
| 09:45 | Opening, 30 minutes: the problems, this repo, the rules, judging. Teams rebalanced for no-shows |
| 10:15 | **Build starts.** Mentors float, about one per three teams |
| 13:00 | Lunch at the tables. Keep building |
| 16:00 | Reminder of submission format. Record your demo early |
| **17:30** | **Hard deadline.** Repo link plus optional 2-minute screen recording |
| 17:35 | Jury and mentors review submissions and pick who presents |
| 18:30 | Final presentations: 6 minutes each plus 4 minutes of questions |
| 19:30 | Jury grades, winners announced, close |

## Rules

1. **No pre-work.** Code you submit must be written from 10:15 today. Libraries, frameworks and your own general tools are fine.
2. **Use any tools.** Claude, Claude Code, Cerebras inference APIs, or anything else that fits.
3. **Use the data in this repo.** You may add other public data. Name it and link it in your README.
4. **No live government systems.** Do not log in to, scrape, or write to any government portal during the build.
5. **No personal data.** The data here has none. Keep it that way.
6. **One workflow, one user, one outcome.** Build the tool for the user in your track's problem statement. Do not build a portal.
7. **Teams of 4 to 5.** Mixed technical and non-technical. Everyone on the team should have real work.
8. **Your repo must be public on GitHub by 17:30.** The code is offered to the department, so it has to be readable.

## Get started in 10 minutes

1. Read your track's `PROBLEM.md`. One page.
2. Read your track's `data/DATA_DICTIONARY.md`.
3. Open the sample file (`*_sample.*`) and look at five rows together as a team.
4. Agree on your user, your one workflow, and what you will demo at 18:30.
5. Split the work. Start building.

## Repo layout

```
README.md                  ← you are here
JUDGING.md                 ← how you are scored
SUBMISSION.md              ← what to submit and how
tracks/
  01-bhumi-vikas-sahayak/
    PROBLEM.md             ← one-page problem statement
    data/                  ← cleaned files, sample, data dictionary
    resources/             ← original PDFs, sample questions
  02-visarjan-ghat-watch/
    PROBLEM.md
    data/
    resources/
tools/                     ← the scripts that made the cleaned data
```

## Questions on the day

Ask a mentor. For anything about the data, check the track's `DATA_DICTIONARY.md` first.

Organisers: Aniket Sahu (Claude Community Ambassador) and Arun Pratap Singh Chandel (Cerebras Community Ambassador).
