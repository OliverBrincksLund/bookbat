def count_words(text):
    return len(text.split())

def count_letters(text):
    """
    Count number of letters in text. Return as dictionary with letter as key and count as value.
    """
    letter_count = {}
    for letter in text:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] = letter_count.get(letter.lower(), 0) + 1
        else:
            letter_count[letter.lower()] = 1
    # print(letter_count)
    return letter_count

def report_generator(letter_count, text, filepath):
    """
    Generate report of letter counts.
    """
    print("============ BOOKBOT REPORT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("----------- Letter Count ----------")
    for letter, count in sorted(letter_count.items(), key=lambda x: x[1], reverse=True):
        if letter.isalpha() or letter == " ":
            #Ignore if letter is a space
            if letter == " ":
                continue
            else:
                print(f"{letter}: {count}")
    print("============ END REPORT ============")