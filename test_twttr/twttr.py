def main():
    word = input("Input: ")
    output = shorten(word)
    print("Output:", output)

def shorten(word):
    output = ""
    for char in word:
        if char.lower() not in "aeiou":
            output += char
    return output

if __name__ == "__main__":
    main()
