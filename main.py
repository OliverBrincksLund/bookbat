from stats import count_words, count_letters, report_generator
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath, encoding='utf-8') as f:
       file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(sys.argv[1]) 
    report_generator(count_letters(text), text, filepath)

if __name__ == "__main__":
    main()