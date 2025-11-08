def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)
    print(f"Found {get_num_words(book_text)} total words")
    

def get_book_text(filepath):

    with open(filepath, 'r', encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words # pyright: ignore[reportMissingImports]

main()
