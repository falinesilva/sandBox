import emoji

# Ask user for a string in English

plaintext = str(input("Input:"))

emojized = emoji.emojize(plaintext)

# Print emojized version of the user input

print (emojized)
