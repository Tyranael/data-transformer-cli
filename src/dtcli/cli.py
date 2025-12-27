from .transforms import trim
import sys

valid_actions = {"trim"}


if len(sys.argv) < 3:
    print("need a valid action AND a text")
    print('Usage: dt <action> "<text>"')
    sys.exit(2)

if sys.argv[1] in valid_actions:
    trimmed = trim(sys.argv[2])
    print(trimmed)
else:
    print(f"Unknown action: {sys.argv[1]}")
    sys.exit(2)
