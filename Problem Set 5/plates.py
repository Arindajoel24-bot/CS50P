def main():
    plate = input("Enter plate: ")

    if is_valid(plate):
       print("Valid")
    else:
       print("Invalid")


def is_valid(character):
    if len(character) < 2 or len(character) > 6:
        return False
    if not character[0:2].isalpha():
        return False
    if not character.isalnum():
        return False
    for i, letter in enumerate(character):
        if letter.isdigit():
           if letter == "0":
               return False
           for remaining in character[i+1:]:
               if remaining.isalpha():
                  return False
           break
    return True
if __name__ == "__main__":
    main()
