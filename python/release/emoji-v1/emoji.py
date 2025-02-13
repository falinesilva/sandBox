import emoji

def main():
    """
    Converts emoji aliases from user input to emojis.
    """
    a = input("Input (use emoji aliases like :smile:): ").strip()
    b = emoji.emojize(a, language='alias')

    if b == a:
        print("No valid emoji found. Use emoji aliases like :smile:.")
    else:
        print(b)

if __name__ == "__main__":
    main()
