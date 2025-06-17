def get_num_words(book_text):
    split_text=book_text.split()
    count=0
    for i in split_text:
        count+=1
    return count

def char_counter(text):
    lower_text=text.lower()
    char_list={}
    char_set=set()
    count=0
    for letter in lower_text:
        #print(f"{letter} to add")
        char_set.add(letter)
        if letter in char_list:
            char_list[letter]+=1
        else:
            char_list[letter]=1
    return char_list

def sort_on(dict):
    return dict["num"]

def better_dict(d):
    new_list=[]
    for char,num in d.items():
        new_list.append({"char": char, "num": num})
    new_list.sort(reverse=True, key=sort_on)
    return new_list 


