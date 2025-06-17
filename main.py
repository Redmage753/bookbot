from stats import get_num_words
from stats import char_counter
from stats import sort_on

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    f.close()
    return content

def main():
    num_words= get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document.")
    #print(get_book_text("books/frankenstein.txt"))
    char_count=char_counter(get_book_text("books/frankenstein.txt"))
    char_count.sort(reverse=True, key=sort_on)    
    print(char_count)

main()
    
