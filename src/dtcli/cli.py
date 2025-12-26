import sys

if len(sys.argv) < 3:
    print("need an action AND a text")
    print('Usage: dt <action> "<text>"')
    sys.exit(2)
print(f"Action received: {sys.argv[1]}\nText received: {sys.argv[2]}")
