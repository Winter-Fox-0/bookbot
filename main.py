from stats import word_counter, char_count
def main():
    maintext = get_book_text("./books/frankenstein.txt")
    print(f"{word_counter(maintext)} words found in the document")
    print(char_count(maintext))
    

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()