# Data Transformer CLI

Small personal project to practice:
- Python fundamentals
- simple data transformations
- clean Git workflow

## Goal
Build a minimal CLI tool that applies small transformations to text-based data.

This project focuses on clarity and structure rather than performance or advanced features.

## MVP (work in progress)
- single transformation at a time
- text input (direct or file)
- output to stdout or file

## Usage (MVP)

The MVP supports a single transformation at a time.

### Trim
dt trim "   hello   "
# output: hello

## Error cases (MVP)

- Missing arguments:
  - dt
  - dt trim
- Unknown transformation:
  - dt foo "hello"


Details will be refined incrementally.
