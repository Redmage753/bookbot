from stats import get_num_words

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    f.close()
    return content

def main():
    num_words= get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document.")
    #print(get_book_text("books/frankenstein.txt"))
    
main()
    
