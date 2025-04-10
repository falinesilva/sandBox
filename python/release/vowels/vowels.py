# Remove the vowels from an input

def main():
    word = input("Input: ")
    output = vowels(word)
    print("Output:", output)

def vowels(word):
    output = ""
    for char in word:
        if char.lower() not in "aeiou":
            output += char
    return output

if __name__ == "__main__":
    main()
