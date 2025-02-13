# Ask user for the answer

answer = input ("What is the Answer to the Great Question of Life, the Universe and Everything? ")

# Remove spaces in front and back and make all lower case
answer = answer.lower().strip()

# If answer is correct, print Yes
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print ("Yes")

# If answer is incorrect, print No
else:
    print ("No")
