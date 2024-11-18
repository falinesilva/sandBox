import emoji

# Ask user for a string in English

a = input("Input: ").strip()

b = emoji.emojize(a, language = 'alias')

# Print emojized version of the user input

print (b)
