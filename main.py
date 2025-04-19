import sys

from stats import get_book_words_count, get_char_count, sort_dict


def get_book_text(book_path):
    with open(book_path) as book:
        book_content = book.read() 
    return book_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = get_book_words_count(get_book_text(sys.argv[1]))
    char_count_dict = get_char_count(get_book_text(sys.argv[1]))
    sorted_list = sort_dict(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_list)):
        if sorted_list[i].get("char").isalpha():
            print(f"{sorted_list[i].get("char")}: {sorted_list[i].get('count')}")


main()
