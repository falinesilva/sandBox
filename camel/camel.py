# Ask user camel case
name = input ("camelCase: ")

# Convert to snake case
s = ""
for c in name:
    if c.isupper():
        s += "_" + c.lower()
    elif c.islower():
        s += c
    else:
        break

# Print snake case
print ("snake_case:",s)
