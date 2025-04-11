def convert(face):
    """Convert a smile or frown to an emoji"""

    # Validate input before replacement
    if ":)" not in face and ":(" not in face:
        print("Error: Invalid input")
        exit(1)

    # Convert emoticons to emojis
    return face.replace(":)", "Yay! 🙂").replace(":(", "Aw 🙁")


def main():
    user_input = input("Are you happy or sad?\nAnswer: ")

    user_input = convert(user_input)

    print(user_input)

if __name__ == "__main__":
    main()