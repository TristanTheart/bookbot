import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    book_text = get_book_text(sys.argv[1])
    counts = count_chars(book_text)
    chars_list = to_list(counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at ")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in chars_list:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")
    print("============= END ===============")


def get_book_text(filepath):

    with open(filepath, 'r', encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words # pyright: ignore[reportMissingImports]
from stats import count_chars # pyright: ignore[reportMissingImports]
from stats import to_list # pyright: ignore[reportMissingImports]

main()
