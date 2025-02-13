import inflect

# Create inflect engine
p = inflect.engine()

# Initialize list of names
names = list()

# Prompt user for names until control-d
try:
    while True:
        names.append(str(input("Name: ").strip()))
except EOFError:
    names = p.join((names))
    print(f"Adieu, adieu, to {names}")
    exit()
