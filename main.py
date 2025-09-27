def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
       file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def main():
    text = get_book_text("books/frankenstein.txt") 
    print(f"Found {count_words(text)} total words")

if __name__ == "__main__":
    main()