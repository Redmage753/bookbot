from stats import get_num_words, char_counter, better_dict

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    f.close()
    return content

def main():
    book="books/frankenstein.txt"
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")

    print(f"----------- Word Count ----------")
    num_words= get_num_words(get_book_text(book))
    print(f"Found {num_words} total words")
    #print(get_book_text("books/frankenstein.txt"))
    
    print(f"--------- Character Count -------")
    char_count=char_counter(get_book_text(book))
    sortable_dict=better_dict(char_count)
    #sortable_dict.sort(reverse=True, key=sort_on)    
    for line in sortable_dict:
        if line["char"].isalpha():
            print(f"{line["char"]}: {line["num"]}")
        else:
            continue
    print(f"============= END ===============")
    #print(sortable_dict)

main()
    
