def get_word_count(book):
    split_book = book.split()
    return len(split_book)

def get_char_count(book):
    split_book = book.split()
    char_dict = {}
    for word in split_book:
        word = word.lower()
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict.update({char: 1})
    sorted_dict = sort_dict(char_dict)
    return sorted_dict

def sort_dict(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
