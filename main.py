def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"--- Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    char_list = sort_on(list(num_chars.items()))
    for char in char_list:
        print(f"The '{char[0]}' character was found {char[1]} times")

def sort_on(char_list):
    return sorted(char_list, key=lambda x: x[1], reverse=True)





def get_num_chars(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_dict:
                char_dict[char] +=1
            else:
                char_dict[char] = 1
    return char_dict


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()