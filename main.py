from stats import get_word_count
from stats import get_char_count

def main():
    num_words = get_word_count()
    char_dict = get_char_count()
    print(f"{num_words} words found in the document")
    print(char_dict)


main()