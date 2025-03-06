from stats import get_word_count, get_char_count
import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text()
    num_words = get_word_count(book)
    char_dict = get_char_count(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_dict:
        if char.isalpha():
            print(f"{char}: {char_dict[char]}")
        else:
            pass
    print("============= END ===============")

main()
