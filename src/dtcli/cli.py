import sys

valid_actions = {"trim"}


if len(sys.argv) < 3:
    print("need a valid action AND a text")
    print('Usage: dt <action> "<text>"')
    sys.exit(2)

if sys.argv[1] in valid_actions:
    print(f"Action received: {sys.argv[1]}\nText received: {sys.argv[2]}")
else:
    print(f"Unknown action: {sys.argv[1]}")
    sys.exit(2)
