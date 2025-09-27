def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
       file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("C:/Github_repositories/bookbot/books/frankenstein.txt") 
    print(text)

if __name__ == "__main__":
    main()