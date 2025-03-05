from stats import get_word_count
from stats import get_char_count

def main():
    num_words = get_word_count()
    char_dict = get_char_count()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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
