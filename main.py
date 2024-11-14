def open_and_print_frankenstein_count_words():
    with open("books/frankenstein.txt") as f:
        # Read the entire content of the file
        file_contents = f.read()

        words_in_frankenstein = count_words_frankenstein(file_contents)

        counted_letter_pairs = count_letters(file_contents)

        # Sort the dictionary by count in descending order
        sorted_counted_letter_pairs = sorted(counted_letter_pairs.items(), key=lambda item: item[1], reverse=True)

        print(f"""--- Begin report of books/frankenstein.txt ---
{words_in_frankenstein} words found in the document\n""")
        for letter, lettercount in sorted_counted_letter_pairs:
            print(f"The \'{letter}\' character was found {lettercount} times")
        print(f"--- End report ---")

def count_words_frankenstein(text_to_count_words):
    counted_words_in_text = text_to_count_words.split()
    return len(counted_words_in_text)

def count_letters(text):
    # Convert the text to lowercase
    text = text.lower()
    # Initialize the dictionary with letters a to z
    letter_count_pairs = {
        "a": 0, "b": 0, "c": 0, "d": 0,
        "e": 0, "f": 0, "g": 0, "h": 0,
        "i": 0, "j": 0, "k": 0, "l": 0,
        "m": 0, "n": 0, "o": 0, "p": 0,
        "q": 0, "r": 0, "s": 0, "t": 0,
        "u": 0, "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0
    }
    # Count each letter in the text
    for character in text:
        if character in letter_count_pairs:
            letter_count_pairs[character] += 1
    return letter_count_pairs

#calling the "main" function
open_and_print_frankenstein_count_words()