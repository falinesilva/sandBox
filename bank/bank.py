# Get greeting from user

greeting = input ("Greeting: ")

# Convert to all lower case

greeting = greeting.lower()

# Print $100 if greeting does not start with h
if greeting.startswith("h") == 0:
    print ("$100")

# Print $20 if greet starts with h but does not equal hello

elif greeting.startswith("h") and greeting.startswith ("hello") == 0:
    print ("$20")

# Otherwise print $0
else:
    print ("$0")

