import sys
from stats import words_in_book, number_of_chars



def get_book_text():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at: " + book_path)
    
    with open(book_path) as book:
        text = book.read()
        words_in_book(text)
        number_of_chars(text)



    
def main():
    get_book_text()

main()