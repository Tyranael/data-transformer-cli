# Plan — Data Transformer CLI

## Goal
Build a minimal CLI tool that applies a single transformation to text input.

## MVP definition (Done when…)
The MVP is considered DONE when the following command works:

dt trim "   hello   "
# output: hello

Notes:
- MVP supports ONE transformation at a time.
- Input is provided directly as text (no file I/O in MVP).
- Output is printed to stdout.
- No dependencies required.

## Non-goals (for MVP)
- reading from files (--in)
- writing to files (--out)
- chaining multiple transformations
- CSV/TSV conversion
- fancy formatting (colors, tables, etc.)
- performance optimizations

---

## Ticket list (atomic tasks)

### MVP-01 — Decide the exact CLI contract for MVP
**Deliverable**
- Update README `Usage (planned)` to reflect the exact MVP command shape.
**Acceptance**
- README shows the exact command we will implement for MVP (transform + text).

### MVP-02 — Replace interactive input with CLI arguments (minimal)
**Deliverable**
- `cli.py` reads `transform` and `text` from command line arguments.
**Acceptance**
- Running the program without arguments prints a helpful usage/error message.
- Running with arguments prints something deterministic (even if transform is not applied yet).

### MVP-03 — Define transformation type(s) (Enum or simple mapping)
**Deliverable**
- Create a single place that lists supported transformations (MVP: only `trim`).
**Acceptance**
- `trim` is recognized as a valid transform.
- Unknown transforms are rejected with a clear message.

### MVP-04 — Implement `trim` transformation (pure function)
**Deliverable**
- Add a pure function that performs trim on a string.
**Acceptance**
- Given `"   hello   "`, output is `"hello"` (no extra whitespace).ls -

### MVP-05 — Wire CLI to transformation logic
**Deliverable**
- `cli.py` routes `trim` to the trim function and prints the result.
**Acceptance**
- `dt trim "   hello   "` prints `hello`.

### MVP-06 — Minimal manual test checklist (no test framework yet)
**Deliverable**
- Add a short checklist in `docs/plan.md` or `README.md` with 4-5 manual cases.
**Acceptance**
- Manual cases cover: normal trim, empty string, only spaces, missing args, unknown transform.

## Manual test checklist (MVP)

- [ ] `python3 src/dtcli/cli.py trim "   hello   "` -> outputs `hello`
- [ ] `python3 src/dtcli/cli.py trim ""` -> outputs empty line
- [ ] `python3 src/dtcli/cli.py trim "     "` -> outputs empty line
- [ ] `python3 src/dtcli/cli.py` -> prints usage and exits with code 2
- [ ] `python3 src/dtcli/cli.py trimp "hello"` -> prints unknown action and exits with code 2


### MVP-07 — Cleanup + docs sync
**Deliverable**
- Ensure README reflects what is actually implemented (not “planned” anymore for trim).
**Acceptance**
- README includes a “Working” usage example for `trim`.
- `git log` history remains clean (small commits, clear messages).

---

## Optional next steps (after MVP)
- V1-01: add `--in` (read text from file)
- V1-02: add `--out` (write output to file)
- V1-03: add `to_csv` / `to_tsv` (define what they mean)
- V1-04: add automated tests (pytest or unittest)
- V1-05: adopt `uv` + pyproject (only if/when dependencies appear)
