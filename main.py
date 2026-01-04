import sys
from stats import get_count_words, count_each_char, sort_list


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_count_words(text) 
    letter_sort = sort_list(text)
    print_report(book_path, num_words,letter_sort)
    

def print_report(book_path, num_words,letter_sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for key, value in letter_sort.items():
        print(f"{key}: {value}")
    print("============= END ===============")

main()