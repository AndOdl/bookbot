def get_book_text(filepath):
    return filepath.read()

def get_word_count(filepath):
    book = get_book_text(filepath)
    split_document = book.split()
    return len(split_document)

def main():
    with open("books/frankenstein.txt") as f:
        print(f"{get_word_count(f)} words found in the document")

main()