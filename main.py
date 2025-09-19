from stats import word_counter, char_count, split
def main():
    book = "./books/frankenstein.txt"
    maintext = get_book_text(book)
    word_count = word_counter(maintext)
    char_dic = split(char_count(maintext))
    #print(char_dic)
    #split(char_dic)
    format(book,word_count,char_dic)
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def format(book,wordcount,charcount):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for char in charcount:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()