def get_book_text(filepath):
    return filepath.read()

def main():
    with open("books/frankenstein.txt") as f:
        print(get_book_text(f))

main()
