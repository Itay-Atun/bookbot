def get_book_words_count(book_text : str) -> int:
    words_in_string = book_text.split()

    return len(words_in_string)

def get_char_count(book_text : str):
    words_num = get_book_words_count(book_text)
    lower_case_text = book_text.lower().split()

    char_count_dict = {}

    for word in range(0, words_num):
        current_word = lower_case_text[word]
        for char in range(0, len(current_word)):
            if current_word[char] in char_count_dict:
                char_count_dict[current_word[char]] += 1
            else:
                char_count_dict[current_word[char]] = 1
    return char_count_dict


def sort_on(dict):
    return dict["count"]

def sort_dict(char_counter_dict):

    sorted_list = []
    for key, value in char_counter_dict.items():
        sorted_list.append({"char":key, "count":value})

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


