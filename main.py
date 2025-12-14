def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()

  return file_contents

def get_word_count(book_string):
    return len(book_string.split())

def main():
    book_string = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_string)
    print(f"Found {num_words} total words")

main()