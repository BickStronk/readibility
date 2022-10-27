# Imports - DO NOT MODIFY
from helper import get_string


def main():
    text = get_string("Text: ")

    num_of_letters = count_letters(text)
    num_of_words = count_words(text) + 1
    num_of_sentences = count_sentences(text)

    L = num_of_letters / num_of_words * 100
    S = num_of_sentences / num_of_words * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    num_of_letters = 0
    for char in text:
        if char.isalpha():
            num_of_letters += 1

    return num_of_letters


def count_words(text):
    num_of_words = 0
    for char in text:
        if char == " ":
            num_of_words += 1

    return num_of_words


def count_sentences(text):
    num_of_sentences = 0
    for char in text:
        if char in ["!", ",", ".", "?"]:
            num_of_sentences += 1

    return num_of_sentences


# DO NOT MODIFY
if __name__ == "__main__":
    main()
