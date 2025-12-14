import sys
from stats import get_word_count, get_character_count, sort_character_count

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()

  return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_string = get_book_text(sys.argv[1])
        num_words = get_word_count(book_string)
        character_count = get_character_count(book_string)
        character_count_sorted = sort_character_count(character_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for character_count in character_count_sorted:
            char = character_count["char"]
            num = character_count["num"]
            if char.isalpha():
                print(f"{char}: {num}")
        print("============= END ===============")

main()