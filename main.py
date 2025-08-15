from typing import Dict
from stats import get_word_count
import sys


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def get_character_count_dict(contents: str) -> Dict[str, int]:
    char_dict: Dict[str, int] = {}
    for c in contents:
        c_lower = c.lower()
        if c_lower in char_dict:
            char_dict[c_lower] += 1
        else:
            char_dict[c_lower] = 1
    return char_dict


def sort_on(dict):
    return dict["count"]


def get_sorted_dict_list(char_dict: Dict[str, int]):
    sorted_dicts = []
    for char in char_dict:
        if char.isalpha():
            sorted_dicts.append({"character": char, "count": char_dict[char]})
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts


def print_sorted_dicts(sorted_dicts):
    for dict in sorted_dicts:
        character = dict["character"]
        count = dict["count"]
        print(f"{character}: {count}")


def main():
    book_path = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    contents = get_book_text(sys.argv[1])
    char_count_dict = get_character_count_dict(contents)
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(contents)} words found in the document")
    print()
    print_sorted_dicts(get_sorted_dict_list(char_count_dict))
    print("--- End report ---")


main()
