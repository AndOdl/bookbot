def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def get_word_count():
    book = get_book_text()
    split_book = book.split()
    return len(split_book)

def get_char_count():
    book = get_book_text()
    split_book = book.split()
    char_dict = {}
    for word in split_book:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict.update({char: 1})
    return char_dict
    