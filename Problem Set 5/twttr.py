def main():
    text = input("Enter text: ")
    print(shorten(text))
def shorten(word):
    for letter in word:
        if letter.lower() in "aeiou":
            word = word.replace(letter, "")

    return word

if __name__ == "__main__":
    main()