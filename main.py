from stats import get_num_words, char_counter, better_dict
import os, sys

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    f.close()
    return content

def default_error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

def main():
    try:
        book=sys.argv[1]
        if not os.path.exists(book):
            raise FileNotFoundError("Location does not exist.")

    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    except FileNotFoundError as e:
        default_error(e)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")

    print(f"----------- Word Count ----------")
    num_words= get_num_words(get_book_text(book))
    print(f"Found {num_words} total words")
    
    print(f"--------- Character Count -------")
    char_count=char_counter(get_book_text(book))

    sortable_dict=better_dict(char_count)

    for line in sortable_dict:
        if line["char"].isalpha():
            print(f"{line["char"]}: {line["num"]}")
        else:
            continue
    print(f"============= END ===============")

main()
    
