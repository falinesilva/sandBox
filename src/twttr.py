text = input("Input: ")

output = ""

for char in text:
    if char.lower() not in "aeiou":
        output += char

print("Output:", output)
