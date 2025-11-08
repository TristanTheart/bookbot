def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

def get_book_text(filepath):

    with open(filepath, 'r', encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents



main()
