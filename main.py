def main():
    book_path = 'books/frankenstrein.txt'
    text = get_book_text(book_path)
    words = count_words(text)
    char_dict = count_character(text)
    print(f"--- Begin report on {book_path} ---")
    print(f"{words} words found in the document")
    display_dict(char_dict)
    print(f"--- End report ---")
    
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def display_dict(dic):
    word_list = []
    for item in dic:
        item_name = item
        item_num = dic[item]
        sentence = f"The {item_name} character was found {item_num} times"
        word_list.append(sentence)

    word_list.sort()
    for sent in word_list:
        print(sent)

   
def count_words(text):
    return len(text.split())


	
def count_character(text):
    string_list = text.split()
    dic = {}
    for word in string_list:
        for char in word:
            lowered = char.lower()
            if lowered in dic:
                dic[lowered] += 1
            else:
                dic[lowered] = 1
    return dic
                

    
main()


